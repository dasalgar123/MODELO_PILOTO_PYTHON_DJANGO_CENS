# Guía: Integración con SharePoint/OneDrive Empresarial

## 📧 ¿Cómo Guardar en SharePoint desde tu Aplicación?

Si tienes un correo empresarial como `DANIEL.SALINAS@cens.co`, puedes integrar tu aplicación Django con SharePoint/OneDrive para guardar archivos automáticamente.

---

## 🎯 OPCIONES DE INTEGRACIÓN

### Opción 1: Guardar Archivos Excel/PDF en SharePoint

**Escenario:** Cuando un inspector completa una inspección, el sistema genera un archivo Excel/PDF y lo guarda automáticamente en SharePoint.

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUJO DE GUARDADO                         │
└─────────────────────────────────────────────────────────────┘

1. Inspector completa inspección
        │
        ▼
2. Sistema genera archivo Excel/PDF
        │
        ▼
3. Sistema se conecta a SharePoint
        │
        ▼
4. Guarda archivo en carpeta específica
        │
        ▼
5. Archivo disponible en SharePoint
   📁 SharePoint/CENS/Inspecciones/2025/12/
   └── 20251212_S30_LaMiel_DanielSalinas.xlsx
```

---

## 🔧 IMPLEMENTACIÓN CON MICROSOFT GRAPH API

### Paso 1: Registrar Aplicación en Azure AD

1. Ve a [Azure Portal](https://portal.azure.com)
2. Azure Active Directory > App registrations
3. New registration
4. Nombre: "Sistema - Subgerencia de Estaciones y Líneas CENS"
5. Redirect URI: `http://localhost:8000/callback`
6. Registrar
7. Copiar:
   - **Application (client) ID**
   - **Directory (tenant) ID**
   - **Client secret** (crear en "Certificates & secrets")

### Paso 2: Instalar Librería en Django

```bash
pip install msal requests
```

### Paso 3: Configurar en settings.py

```python
# settings.py

# Configuración SharePoint/OneDrive
SHAREPOINT_CONFIG = {
    'CLIENT_ID': 'tu-client-id',
    'CLIENT_SECRET': 'tu-client-secret',
    'TENANT_ID': 'tu-tenant-id',
    'SITE_URL': 'https://cens.sharepoint.com/sites/Inspecciones',
    'FOLDER_PATH': '/sites/Inspecciones/Documentos/Inspecciones'
}
```

### Paso 4: Crear Función para Subir Archivo

```python
# app/utils/sharepoint.py

import requests
from msal import ConfidentialClientApplication
from django.conf import settings

def get_access_token():
    """Obtener token de acceso de Microsoft Graph"""
    app = ConfidentialClientApplication(
        client_id=settings.SHAREPOINT_CONFIG['CLIENT_ID'],
        client_credential=settings.SHAREPOINT_CONFIG['CLIENT_SECRET'],
        authority=f"https://login.microsoftonline.com/{settings.SHAREPOINT_CONFIG['TENANT_ID']}"
    )
    
    result = app.acquire_token_for_client(
        scopes=["https://graph.microsoft.com/.default"]
    )
    
    return result.get('access_token')

def upload_to_sharepoint(file_path, file_name, folder_path=None):
    """Subir archivo a SharePoint"""
    
    # Obtener token
    token = get_access_token()
    
    # URL de la API de Microsoft Graph
    site_url = settings.SHAREPOINT_CONFIG['SITE_URL']
    folder = folder_path or settings.SHAREPOINT_CONFIG['FOLDER_PATH']
    
    # Endpoint para subir archivo
    upload_url = f"https://graph.microsoft.com/v1.0/sites/{site_url}/drive/root:/{folder}/{file_name}:/content"
    
    # Leer archivo
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    # Headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/octet-stream'
    }
    
    # Subir archivo
    response = requests.put(upload_url, headers=headers, data=file_content)
    
    if response.status_code == 200 or response.status_code == 201:
        return {
            'success': True,
            'url': response.json().get('webUrl'),
            'message': 'Archivo subido exitosamente a SharePoint'
        }
    else:
        return {
            'success': False,
            'error': response.text
        }
```

### Paso 5: Usar en tu Vista

```python
# app/views.py

from .utils.sharepoint import upload_to_sharepoint
import os
from datetime import datetime

def guardar_inspeccion_con_sharepoint(request):
    # ... tu lógica para guardar inspección ...
    
    # Generar archivo Excel
    excel_path = generar_excel_inspeccion(inspeccion)
    
    # Nombre del archivo
    fecha = datetime.now().strftime('%Y%m%d')
    inspector = request.session.get('inspector_nombre', 'Desconocido')
    subestacion = inspeccion.subestacion
    file_name = f"{fecha}_{subestacion}_{inspector}.xlsx"
    
    # Subir a SharePoint
    resultado = upload_to_sharepoint(
        file_path=excel_path,
        file_name=file_name,
        folder_path=f"/Inspecciones/{datetime.now().year}/{datetime.now().month:02d}/"
    )
    
    if resultado['success']:
        # Guardar URL de SharePoint en base de datos
        inspeccion.sharepoint_url = resultado['url']
        inspeccion.save()
        
        return render(request, 'success.html', {
            'message': 'Inspección guardada y subida a SharePoint',
            'sharepoint_url': resultado['url']
        })
    else:
        # Manejar error
        return render(request, 'error.html', {
            'error': 'Error al subir a SharePoint: ' + resultado['error']
        })
```

---

## 📁 ESTRUCTURA EN SHAREPOINT

```
SharePoint - CENS
└── Documentos
    └── Inspecciones
        ├── 2025
        │   ├── 01 (Enero)
        │   │   ├── 20250112_S30_LaMiel_DanielSalinas.xlsx
        │   │   └── 20250113_S_XX_Zulia_JuanPerez.xlsx
        │   ├── 02 (Febrero)
        │   └── 12 (Diciembre)
        │       ├── 20251212_S30_LaMiel_DanielSalinas.xlsx
        │       └── 20251213_S01_CarlosLopez.xlsx
        └── 2026
```

---

## 🔐 PERMISOS Y SEGURIDAD

### Permisos Necesarios en Azure AD:

1. **Files.ReadWrite.All** - Leer y escribir archivos
2. **Sites.ReadWrite.All** - Acceso a sitios de SharePoint
3. **User.Read** - Leer información del usuario

### Configuración de Permisos:

1. En Azure Portal > App registrations > Tu app
2. API permissions
3. Add a permission > Microsoft Graph
4. Application permissions
5. Seleccionar permisos necesarios
6. Grant admin consent

---

## 🎯 ALTERNATIVA MÁS SIMPLE: OneDrive Personal

Si solo necesitas guardar en el OneDrive personal del usuario:

```python
def upload_to_onedrive(file_path, file_name, user_email):
    """Subir a OneDrive personal del usuario"""
    
    # Obtener token del usuario
    token = get_user_token(user_email)
    
    # Subir a OneDrive del usuario
    upload_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/Inspecciones/{file_name}:/content"
    
    # ... resto del código similar ...
```

---

## 📊 DIAGRAMA DE FLUJO COMPLETO

```
┌─────────────────────────────────────────────────────────────┐
│              FLUJO CON INTEGRACIÓN SHAREPOINT               │
└─────────────────────────────────────────────────────────────┘

1. Inspector completa inspección
        │
        ▼
2. Sistema guarda en Base de Datos local
        │
        ▼
3. Sistema genera archivo Excel/PDF
        │
        ▼
4. Sistema se autentica con Microsoft Graph API
        │
        ▼
5. Sistema sube archivo a SharePoint
   📁 SharePoint/CENS/Inspecciones/2025/12/
        │
        ▼
6. Sistema guarda URL de SharePoint en BD
        │
        ▼
7. Administrador puede:
   • Ver archivo en SharePoint
   • Descargar desde SharePoint
   • Acceder desde cualquier dispositivo
```

---

## ✅ VENTAJAS DE INTEGRAR CON SHAREPOINT

1. **Backup Automático**: Archivos guardados en la nube
2. **Acceso desde Cualquier Lugar**: Disponible en SharePoint online
3. **Colaboración**: Múltiples usuarios pueden acceder
4. **Versionado**: SharePoint mantiene historial de versiones
5. **Búsqueda**: Búsqueda avanzada en SharePoint
6. **Seguridad**: Control de acceso empresarial
7. **Integración**: Compatible con Office 365

---

## 🔄 ALTERNATIVA: Guardar Solo URL en SharePoint

Si prefieres no subir archivos automáticamente, puedes:

1. Generar el archivo localmente
2. Crear un enlace en SharePoint que apunte al archivo
3. Guardar solo la referencia/URL

---

## 📝 CONFIGURACIÓN EN DIAGRAMAS

En los diagramas del sistema, se debe mostrar:

```
┌─────────────────────────────────────────────────────────────┐
│              GUARDADO DE INSPECCIONES                        │
└─────────────────────────────────────────────────────────────┘

Al guardar inspección:
    │
    ├─> Guardar en Base de Datos Local
    │
    └─> Generar Archivo Excel/PDF
            │
            └─> Subir a SharePoint
                    │
                    └─> Guardar URL en BD
```

---

## 🚀 IMPLEMENTACIÓN PASO A PASO

### Paso 1: Obtener Credenciales
- Registrar app en Azure AD
- Obtener Client ID, Secret, Tenant ID

### Paso 2: Instalar Dependencias
```bash
pip install msal requests
```

### Paso 3: Configurar en Django
- Agregar configuración en settings.py
- Crear función de subida

### Paso 4: Integrar en Vistas
- Llamar función después de guardar inspección
- Manejar errores

### Paso 5: Probar
- Probar con archivo de prueba
- Verificar que aparece en SharePoint

---

## ⚠️ IMPORTANTE

- **Autenticación**: Necesitas permisos de administrador en Azure AD
- **Credenciales**: Guarda las credenciales de forma segura (variables de entorno)
- **Errores**: Implementa manejo de errores robusto
- **Testing**: Prueba primero en ambiente de desarrollo

---

**Fecha de creación**: 12 de diciembre de 2025  
**Versión**: 1.0

