# Cómo el Administrador Ve Archivos/Inspecciones desde Drive

## 🎯 Pregunta: ¿Cómo hace el administrador para ver los archivos o inspecciones llenadas desde Drive?

---

## 📊 OPCIONES PARA QUE EL ADMINISTRADOR VEA LOS ARCHIVOS

### Opción 1: SharePoint Site (Recomendada para Administrador) ⭐

**Ventaja:** Todos los archivos en un solo lugar compartido, el administrador ve todo.

#### Cómo Funciona:

```
Inspector guarda inspección
        │
        ▼
Sistema sube a SharePoint Site
📁 SharePoint/CENS/Inspecciones/2025/12/
└── 20251212_S30_LaMiel_DanielSalinas.xlsx
        │
        ▼
Administrador accede a SharePoint
✅ Ve TODOS los archivos
✅ Puede descargar
✅ Puede buscar
✅ Puede filtrar
```

#### Configuración:

```python
# Guardar en SharePoint Site (compartido)
def upload_to_sharepoint_site(file_path, file_name):
    """
    Sube a SharePoint Site (todos pueden ver)
    """
    token = get_app_token()
    
    # URL de SharePoint Site
    site_url = "https://cens.sharepoint.com/sites/Inspecciones"
    folder_path = f"/Inspecciones/{datetime.now().year}/{datetime.now().month:02d}/"
    
    upload_url = f"https://graph.microsoft.com/v1.0/sites/{site_url}/drive/root:{folder_path}{file_name}:/content"
    
    # ... subir archivo ...
```

#### Acceso del Administrador:

1. **Ir a SharePoint:**
   - URL: `https://cens.sharepoint.com/sites/Inspecciones`
   - Login con correo corporativo (@cens.com.co)

2. **Ver Archivos:**
   - Carpeta: `/Inspecciones/2025/12/`
   - Ve todos los archivos de todos los inspectores
   - Puede filtrar por fecha, inspector, subestación

3. **Acciones Disponibles:**
   - ✅ Ver archivo online
   - ✅ Descargar
   - ✅ Compartir
   - ✅ Buscar
   - ✅ Filtrar

**Ventaja:** El administrador ve TODO en un solo lugar.

---

### Opción 2: OneDrive Personal + Acceso Compartido

**Ventaja:** Cada inspector tiene su carpeta, pero el administrador puede acceder.

#### Cómo Funciona:

```
Inspector guarda inspección
        │
        ▼
Sistema sube a OneDrive Personal del Inspector
📁 OneDrive (daniel.salinas@cens.com.co)
└── Documents/subestaciones proyecto digital cens/
    └── 20251212_S30_LaMiel.xlsx
        │
        ▼
Inspector comparte carpeta con Administrador
        │
        ▼
Administrador tiene acceso
✅ Ve archivos del inspector
```

#### Configuración:

**Paso 1: Inspector comparte carpeta**
1. Inspector va a su OneDrive
2. Carpeta: `Documents/subestaciones proyecto digital cens`
3. Click derecho → Compartir
4. Comparte con: `admin@cens.com.co`
5. Permisos: "Editor" o "Lector"

**Paso 2: Administrador accede**
1. Administrador recibe notificación
2. Accede a carpeta compartida
3. Ve archivos del inspector

**Desventaja:** El administrador debe tener acceso a cada OneDrive individual.

---

### Opción 3: Base de Datos + URL de Drive (Mejor Opción) ⭐⭐⭐

**Ventaja:** El administrador ve todo desde el sistema, con enlaces directos a Drive.

#### Cómo Funciona:

```
Inspector guarda inspección
        │
        ├─> Guarda en Base de Datos
        │   └─> Datos de la inspección
        │
        └─> Sube a OneDrive/SharePoint
            └─> Guarda URL en Base de Datos
                └─> inspeccion.onedrive_url = "https://..."
                    │
                    ▼
Administrador ve en Sistema
✅ Lista de inspecciones
✅ Datos completos
✅ Enlace directo a archivo en Drive
✅ Click → Abre archivo en Drive
```

#### Implementación en Código:

```python
# views.py - Al guardar inspección
def guardar_inspeccion(request):
    # Guardar datos
    inspeccion = guardar_datos(request)
    
    # Generar Excel
    excel_path = generar_excel(inspeccion)
    file_name = f"{fecha}_{subestacion}_{inspector}.xlsx"
    
    # Subir a OneDrive/SharePoint
    resultado = upload_to_onedrive(excel_path, file_name, inspector_email)
    
    if resultado['success']:
        # Guardar URL en base de datos
        inspeccion.onedrive_url = resultado['url']  # ← URL del archivo
        inspeccion.save()
    
    return redirect('menu')
```

#### Vista del Administrador:

```python
# views.py - Vista para administrador
def ver_inspecciones_admin(request):
    """
    El administrador ve todas las inspecciones
    """
    # Obtener todas las inspecciones
    inspecciones = Inspeccion.objects.all().order_by('-fecha_ejecucion')
    
    return render(request, 'admin/inspecciones.html', {
        'inspecciones': inspecciones
    })
```

#### Template HTML para Administrador:

```html
<!-- admin/inspecciones.html -->
<table>
    <thead>
        <tr>
            <th>Fecha</th>
            <th>Inspector</th>
            <th>Subestación</th>
            <th>Estado</th>
            <th>Archivo Drive</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for inspeccion in inspecciones %}
        <tr>
            <td>{{ inspeccion.fecha_ejecucion|date:"d/m/Y" }}</td>
            <td>{{ inspeccion.inspector.nombre }}</td>
            <td>{{ inspeccion.subestacion }}</td>
            <td>{{ inspeccion.estado }}</td>
            <td>
                {% if inspeccion.onedrive_url %}
                    <a href="{{ inspeccion.onedrive_url }}" target="_blank">
                        📁 Ver en Drive
                    </a>
                {% else %}
                    <span>No disponible</span>
                {% endif %}
            </td>
            <td>
                <a href="{% url 'ver_inspeccion' inspeccion.id %}">Ver Detalles</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Ventaja:** El administrador ve todo desde el sistema con enlaces directos.

---

## 🎯 RECOMENDACIÓN: Sistema Híbrido

### Mejor Solución: Base de Datos + SharePoint Site

```
┌─────────────────────────────────────────────────────────┐
│              SISTEMA COMPLETO                           │
└─────────────────────────────────────────────────────────┘

1. Inspector guarda inspección
        │
        ├─> Guarda en Base de Datos
        │   └─> Datos completos
        │
        └─> Sube a SharePoint Site
            └─> Guarda URL en Base de Datos
                └─> inspeccion.sharepoint_url
                    │
                    ▼
2. Administrador accede al Sistema
        │
        ├─> Ve lista de inspecciones (Base de Datos)
        │   └─> Filtros: fecha, inspector, subestación
        │
        └─> Click en "Ver en SharePoint"
            └─> Abre archivo en SharePoint
                └─> Puede descargar, ver, compartir
```

---

## 📋 IMPLEMENTACIÓN COMPLETA

### Paso 1: Modelo de Base de Datos

```python
# models.py
class Inspeccion(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    subestacion = models.CharField(max_length=100)
    fecha_ejecucion = models.DateTimeField()
    estado = models.CharField(max_length=20)
    datos_inspeccion = models.JSONField()
    
    # URLs de archivos en Drive
    onedrive_url = models.URLField(blank=True, null=True)
    sharepoint_url = models.URLField(blank=True, null=True)
    
    # Tiempo de ejecución (solo admin ve)
    tiempo_inicio = models.DateTimeField(blank=True, null=True)
    tiempo_fin = models.DateTimeField(blank=True, null=True)
    duracion_segundos = models.IntegerField(blank=True, null=True)
    duracion_formato = models.CharField(max_length=50, blank=True, null=True)
```

### Paso 2: Vista del Administrador

```python
# views.py
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.tipo_usuario == 'Administrador'

@user_passes_test(is_admin)
def admin_ver_inspecciones(request):
    """
    Vista para que el administrador vea todas las inspecciones
    """
    # Obtener todas las inspecciones
    inspecciones = Inspeccion.objects.all().order_by('-fecha_ejecucion')
    
    # Filtros opcionales
    inspector_filter = request.GET.get('inspector')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    subestacion_filter = request.GET.get('subestacion')
    
    if inspector_filter:
        inspecciones = inspecciones.filter(inspector__username=inspector_filter)
    if fecha_desde:
        inspecciones = inspecciones.filter(fecha_ejecucion__gte=fecha_desde)
    if fecha_hasta:
        inspecciones = inspecciones.filter(fecha_ejecucion__lte=fecha_hasta)
    if subestacion_filter:
        inspecciones = inspecciones.filter(subestacion=subestacion_filter)
    
    return render(request, 'admin/inspecciones.html', {
        'inspecciones': inspecciones,
        'inspectores': User.objects.filter(tipo_usuario='Inspector'),
        'subestaciones': ['S30_LaMiel', 'S_XX_Zulia', 'S01'],
    })
```

### Paso 3: Template HTML

```html
<!-- admin/inspecciones.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Gestión de Inspecciones - Administrador</h1>

<!-- Filtros -->
<form method="get" class="filtros">
    <select name="inspector">
        <option value="">Todos los inspectores</option>
        {% for inspector in inspectores %}
        <option value="{{ inspector.username }}">{{ inspector.nombre }}</option>
        {% endfor %}
    </select>
    
    <input type="date" name="fecha_desde" placeholder="Fecha desde">
    <input type="date" name="fecha_hasta" placeholder="Fecha hasta">
    
    <select name="subestacion">
        <option value="">Todas las subestaciones</option>
        {% for sub in subestaciones %}
        <option value="{{ sub }}">{{ sub }}</option>
        {% endfor %}
    </select>
    
    <button type="submit">🔍 Buscar</button>
</form>

<!-- Tabla de Inspecciones -->
<table class="tabla-inspecciones">
    <thead>
        <tr>
            <th>Fecha</th>
            <th>Inspector</th>
            <th>Subestación</th>
            <th>Estado</th>
            <th>Duración</th>
            <th>Archivo Drive</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for inspeccion in inspecciones %}
        <tr>
            <td>{{ inspeccion.fecha_ejecucion|date:"d/m/Y H:i" }}</td>
            <td>{{ inspeccion.inspector.nombre }}</td>
            <td>{{ inspeccion.subestacion }}</td>
            <td>
                <span class="estado {{ inspeccion.estado|lower }}">
                    {{ inspeccion.estado }}
                </span>
            </td>
            <td>
                {% if inspeccion.duracion_formato %}
                    ⏱️ {{ inspeccion.duracion_formato }}
                {% else %}
                    -
                {% endif %}
            </td>
            <td>
                {% if inspeccion.sharepoint_url %}
                    <a href="{{ inspeccion.sharepoint_url }}" 
                       target="_blank" 
                       class="btn-ver-drive">
                        📁 Ver en SharePoint
                    </a>
                {% elif inspeccion.onedrive_url %}
                    <a href="{{ inspeccion.onedrive_url }}" 
                       target="_blank" 
                       class="btn-ver-drive">
                        📁 Ver en OneDrive
                    </a>
                {% else %}
                    <span class="sin-archivo">No disponible</span>
                {% endif %}
            </td>
            <td>
                <a href="{% url 'ver_detalles' inspeccion.id %}">Ver Detalles</a>
                <a href="{% url 'descargar_excel' inspeccion.id %}">📥 Descargar</a>
            </td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="7">No hay inspecciones registradas</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---

## 🔍 BÚSQUEDA AVANZADA PARA ADMINISTRADOR

### Funcionalidades:

1. **Filtrar por Inspector:**
   - Ver todas las inspecciones de un inspector específico
   - Comparar productividad entre inspectores

2. **Filtrar por Fecha:**
   - Ver inspecciones de un día específico
   - Ver inspecciones en un rango de fechas

3. **Filtrar por Subestación:**
   - Ver todas las inspecciones de S30 La Miel
   - Ver todas las inspecciones de S_XX Zulia

4. **Ver Tiempo de Ejecución:**
   - Duración de cada inspección
   - Tiempo promedio por inspector
   - Tiempo promedio por subestación

5. **Acceso Directo a Archivos:**
   - Click en "Ver en SharePoint" → Abre archivo
   - Click en "Descargar" → Descarga Excel
   - Ver detalles completos de la inspección

---

## 📊 VISTA DE TABLA PARA ADMINISTRADOR

```
┌─────────────────────────────────────────────────────────────────────────────┐
│        TABLA DE INSPECCIONES (SOLO ADMINISTRADOR)                            │
├──────────────┬───────────────┬──────────────┬──────────┬──────────┬─────────┤
│   Fecha      │  Inspector    │  Subestación │  Estado  │ Duración │  Drive  │
├──────────────┼───────────────┼──────────────┼──────────┼──────────┼─────────┤
│ 12/12/2025   │ D. Salinas    │ S30-La Miel  │Completada│ 1h 23m  │ 📁 Ver  │
│ 11/12/2025   │ J. Pérez      │ S_XX-Zulia   │Completada│ 45m 12s  │ 📁 Ver  │
│ 10/12/2025   │ C. López      │ S01          │Completada│ 2h 15m   │ 📁 Ver  │
└──────────────┴───────────────┴──────────────┴──────────┴──────────┴─────────┘
```

**Cada fila tiene:**
- ✅ Datos de la inspección
- ✅ Enlace directo a archivo en Drive
- ✅ Botón para ver detalles
- ✅ Botón para descargar

---

## 🎯 FLUJO COMPLETO PARA ADMINISTRADOR

```
1. Administrador hace login
        │
        ▼
2. Accede a "Gestión de Inspecciones"
        │
        ▼
3. Ve tabla con TODAS las inspecciones
        │
        ├─> Puede filtrar por:
        │   • Inspector
        │   • Fecha
        │   • Subestación
        │   • Rango de fechas
        │
        ▼
4. Click en "Ver en SharePoint"
        │
        ▼
5. Se abre archivo en SharePoint
        │
        ├─> Puede:
        │   • Ver archivo online
        │   • Descargar
        │   • Compartir
        │   • Editar (si tiene permisos)
```

---

## ✅ VENTAJAS DE ESTA SOLUCIÓN

### Para el Administrador:

1. ✅ **Ve todo en un solo lugar**
   - Tabla con todas las inspecciones
   - Filtros avanzados
   - Búsqueda rápida

2. ✅ **Acceso directo a archivos**
   - Click → Abre en SharePoint
   - No necesita buscar manualmente
   - Enlaces siempre actualizados

3. ✅ **Información completa**
   - Datos de la inspección
   - Tiempo de ejecución
   - Estado
   - Inspector responsable

4. ✅ **Acciones disponibles**
   - Ver detalles
   - Descargar Excel
   - Exportar a PDF
   - Compartir archivo

---

## 📝 RESUMEN

### ¿Cómo ve el administrador los archivos?

**Opción Recomendada: Sistema + SharePoint**

1. **Desde el Sistema Django:**
   - Tabla con todas las inspecciones
   - Filtros avanzados
   - Enlaces directos a archivos

2. **Desde SharePoint:**
   - Todos los archivos en carpeta compartida
   - Acceso directo con correo corporativo
   - Puede descargar, ver, compartir

3. **Flujo:**
   ```
   Admin → Sistema Django → Ver lista → Click en "Ver en SharePoint" → Abre archivo
   ```

### Ventajas:

- ✅ Ve todo desde el sistema
- ✅ Enlaces directos a archivos
- ✅ Filtros y búsqueda avanzada
- ✅ Acceso a SharePoint también disponible
- ✅ Información completa (datos + archivos)

---

**Fecha de creación:** 12 de diciembre de 2025  
**Versión:** 1.0

