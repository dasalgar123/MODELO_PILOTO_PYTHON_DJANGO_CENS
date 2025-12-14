# Formato de Archivos: Drive y Archivo Final

## 📄 Pregunta: ¿En qué formato se sube al Drive y qué formato tiene el archivo final?

---

## 🎯 Respuesta Rápida

### **Formato del Archivo:**
- **Extensión:** `.xlsx` (Excel)
- **Tipo MIME:** `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- **Formato de subida:** `application/octet-stream` (binario)

### **Archivo Final:**
- **Nombre:** `YYYYMMDD_HHMMSS_PREFIJO.xlsx`
- **Ejemplo:** `20251212_143025_S30_LAMIEL.xlsx`
- **Formato:** Excel (.xlsx) - Microsoft Excel Open XML

---

## 📊 Flujo Completo del Formato

```
1. Inspector completa formulario
        │
        ▼
2. Sistema genera archivo Excel (.xlsx)
   └─> Formato: Excel Open XML
   └─> Usa: openpyxl library
        │
        ▼
3. Se guarda localmente
   └─> Carpeta: EXCEL_GUARDADOS/
   └─> Formato: .xlsx (Excel)
        │
        ▼
4. Se sube a OneDrive/SharePoint
   └─> Formato de envío: application/octet-stream (binario)
   └─> Formato final en Drive: .xlsx (Excel)
        │
        ▼
5. Archivo disponible en OneDrive
   └─> Formato: .xlsx (Excel)
   └─> Se puede abrir con Excel, Google Sheets, etc.
```

---

## 🔍 Detalles Técnicos

### 1. **Generación del Archivo (views.py)**

```python
# Línea 926: Nombre del archivo
new_excel_file_name = f"{timestamp}_{file_prefix}.xlsx"
# Ejemplo: "20251212_143025_S30_LAMIEL.xlsx"

# Línea 933: Crear archivo temporal
temp_excel = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
# Formato: .xlsx (Excel)

# Línea 939: Cargar template Excel
workbook = openpyxl.load_workbook(excel_template_path)
# Usa: openpyxl (librería para Excel)

# Línea 1056: Guardar Excel
workbook.save(temp_excel_path)
# Formato guardado: .xlsx (Excel Open XML)
```

**Formato:** `.xlsx` (Excel Open XML Format)

---

### 2. **Guardado Local (EXCEL_GUARDADOS/)**

```python
# Línea 1063-1066: Guardar en carpeta local
excel_guardados_dir = os.path.join(settings.BASE_DIR, 'EXCEL_GUARDADOS')
excel_final_path = os.path.join(excel_guardados_dir, new_excel_file_name)
shutil.copy2(temp_excel_path, excel_final_path)
```

**Ubicación:** `EXCEL_GUARDADOS/20251212_143025_S30_LAMIEL.xlsx`  
**Formato:** `.xlsx` (Excel)

---

### 3. **Descarga al Usuario (HTTP Response)**

```python
# Línea 1108: Content-Type para descarga
response = HttpResponse(
    excel_bytes, 
    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)
```

**Content-Type:** `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`  
**Formato:** Excel Open XML (`.xlsx`)

---

### 4. **Subida a OneDrive/SharePoint**

```python
# Según GUIA_ONEDRIVE_PERSONAL_CORPORATIVO.md línea 127
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/octet-stream'  # ← Formato de envío
}

# El archivo se lee en binario
with open(file_path, 'rb') as file:
    file_content = file.read()  # Bytes binarios
```

**Formato de Envío:** `application/octet-stream` (binario)  
**Formato Final en Drive:** `.xlsx` (Excel)

---

## 📋 Resumen de Formatos

| Etapa | Formato | Descripción |
|-------|---------|-------------|
| **Generación** | `.xlsx` | Excel Open XML (openpyxl) |
| **Guardado Local** | `.xlsx` | Excel en carpeta EXCEL_GUARDADOS/ |
| **Descarga HTTP** | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` | Content-Type para descarga |
| **Subida a Drive** | `application/octet-stream` | Formato binario para transferencia |
| **Archivo en Drive** | `.xlsx` | Excel (se puede abrir con Excel, Google Sheets, etc.) |

---

## 🎯 Formato Final en OneDrive

### **Cuando el archivo llega a OneDrive:**

```
📁 OneDrive Personal (daniel.salinas@cens.com.co)
└── Documents
    └── subestaciones proyecto digital cens
        └── 20251212_143025_S30_LAMIEL.xlsx  ← Formato: .xlsx (Excel)
```

**Características:**
- ✅ **Extensión:** `.xlsx`
- ✅ **Tipo:** Microsoft Excel Open XML
- ✅ **Se puede abrir con:**
  - Microsoft Excel
  - Google Sheets (online)
  - LibreOffice Calc
  - Excel Online (Office 365)
- ✅ **Tamaño:** Depende del contenido (generalmente 50-500 KB)

---

## 🔧 Detalles Técnicos del Formato Excel

### **Excel Open XML (.xlsx):**

**Estructura:**
```
archivo.xlsx (es un ZIP)
├── [Content_Types].xml
├── _rels/
├── docProps/
├── xl/
│   ├── workbook.xml
│   ├── styles.xml
│   ├── sharedStrings.xml
│   └── worksheets/
│       └── sheet1.xml
└── ...
```

**Ventajas:**
- ✅ Formato estándar abierto
- ✅ Compatible con Excel 2007+
- ✅ Más pequeño que .xls antiguo
- ✅ Soporta imágenes, fórmulas, formatos

---

## 📊 Ejemplo de Nombre de Archivo

### **Formato del Nombre:**

```python
# Patrón:
{timestamp}_{file_prefix}.xlsx

# Ejemplo:
20251212_143025_S30_LAMIEL.xlsx
│        │       │
│        │       └─> Prefijo del formulario (S30_LAMIEL)
│        └─> Hora (14:30:25)
└─> Fecha (2025-12-12)
```

### **Desglose:**
- **Fecha:** `20251212` = 12 de diciembre de 2025
- **Hora:** `143025` = 14:30:25 (2:30:25 PM)
- **Prefijo:** `S30_LAMIEL` = Subestación 30 La Miel
- **Extensión:** `.xlsx` = Excel

---

## 🔄 Conversión de Formatos (Si Necesitas)

### **Si quisieras cambiar el formato:**

#### Opción 1: Mantener Excel pero cambiar extensión
```python
# Cambiar a .xls (Excel antiguo) - NO recomendado
# Requiere: xlwt library
```

#### Opción 2: Convertir a PDF
```python
# Requiere: reportlab o weasyprint
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Convertir Excel a PDF
```

#### Opción 3: Convertir a CSV
```python
# Requiere: pandas
import pandas as pd

df = pd.read_excel('archivo.xlsx')
df.to_csv('archivo.csv', index=False)
```

**Recomendación:** Mantener `.xlsx` porque:
- ✅ Es el formato estándar
- ✅ Compatible con Excel
- ✅ Soporta imágenes y formatos
- ✅ Funciona bien con OneDrive

---

## ✅ Resumen Final

### **Formato del Archivo:**

1. **Durante Generación:**
   - Formato: `.xlsx` (Excel Open XML)
   - Librería: `openpyxl`

2. **Guardado Local:**
   - Formato: `.xlsx` (Excel)
   - Ubicación: `EXCEL_GUARDADOS/`

3. **Descarga al Usuario:**
   - Content-Type: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
   - Formato: `.xlsx` (Excel)

4. **Subida a OneDrive:**
   - Formato de envío: `application/octet-stream` (binario)
   - Formato final: `.xlsx` (Excel)

5. **Archivo Final en OneDrive:**
   - Formato: `.xlsx` (Excel)
   - Se puede abrir con Excel, Google Sheets, etc.

### **Conclusión:**

✅ **El archivo SIEMPRE es `.xlsx` (Excel)**  
✅ **Se sube como binario (`application/octet-stream`)**  
✅ **Llega a OneDrive como `.xlsx` (Excel)**  
✅ **Se puede abrir con cualquier programa que lea Excel**

---

## 📝 Ejemplo Visual

```
Inspector guarda inspección
        │
        ▼
Sistema genera:
📄 20251212_143025_S30_LAMIEL.xlsx
   │
   ├─> Guardado local: EXCEL_GUARDADOS/
   │   └─> Formato: .xlsx
   │
   ├─> Descarga al usuario:
   │   └─> Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
   │
   └─> Subida a OneDrive:
       ├─> Envío: application/octet-stream (binario)
       └─> Final: .xlsx (Excel)
           └─> Se puede abrir con Excel, Google Sheets, etc.
```

---

**Fecha de creación:** 12 de diciembre de 2025  
**Versión:** 1.0

