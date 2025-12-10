# ============================================================================
# MAPEO PARA FORMULARIO S01
# ============================================================================
# INSTRUCCIONES PARA COMPLETAR EL MAPEO:
# 1. En el HTML (s01.html), cada campo tiene un atributo "name"
# 2. Aquí debes crear una entrada por cada campo con: "name": "celda_excel"
# 3. Ejemplo: Si en HTML tienes <input name="mi_campo">, aquí pon: "mi_campo": "A10"
# 4. La celda Excel (ej: "A10", "B5", "AN4") es donde quieres que se guarde el valor
#
# IMPORTANTE:
# - El nombre del campo debe coincidir EXACTAMENTE con el "name" del HTML
# - Las celdas Excel pueden ser mayúsculas o minúsculas: "A10" o "a10" funcionan igual
# ============================================================================
s01_mapping = {
    # ========== ENCABEZADO (generalmente igual en todos los formularios) ==========
    "fecha": "AN4",        # Ajustar según tu Excel S01
    "ejecuto": "j5",       # Ajustar según tu Excel S01
    "numero_ot": "J4",     # Ajustar según tu Excel S01
    
    # ========== CAMPOS ESPECÍFICOS DEL FORMULARIO S01 ==========
    # Agrega aquí todos los campos de tu formulario S01
    # Formato: "nombre_del_campo_html": "celda_excel"
    # 
    # EJEMPLO (borra esto y agrega tus campos reales):
    "campo_s01_1": "A10",              # Campo de ejemplo - REEMPLAZAR
    "campo_s01_2": "B10",              # Campo de ejemplo - REEMPLAZAR
    "campo_s01_observaciones": "C10",  # Campo de ejemplo - REEMPLAZAR
    
    # ========== INSTRUCCIONES PASO A PASO ==========
    # 1. Abre tu archivo Excel del formulario S01
    # 2. Identifica dónde quieres guardar cada campo
    # 3. Anota la celda (ej: fila 10, columna A = "A10")
    # 4. En el HTML, asegúrate de que el campo tenga ese "name"
    # 5. Agrega aquí: "nombre_del_campo": "celda_excel"
    #
    # EJEMPLO COMPLETO:
    # Si en tu Excel, en la celda D15 quieres guardar "Temperatura":
    # - En HTML: <input name="temperatura" ...>
    # - Aquí: "temperatura": "D15"
    #
    # ========== AGREGA TUS CAMPOS AQUÍ ==========
}

# ============================================================================
# CONFIGURACIÓN DEL FORMULARIO S01
# ============================================================================
S01_CONFIG = {
    'mapping': s01_mapping,
    'template': 'subestacion/S01/s01.html',
    'excel_template': 'C:\\Users\\ANDRES\\Desktop\\la miel\\app\\templates\\EXEL\\S01_TEMPLATE.xlsx',  # ⚠️ CAMBIAR: Ruta completa a tu Excel S01
    'excel_sheet': 'HOJA1',      # ⚠️ CAMBIAR: Nombre exacto de la hoja Excel
    'file_prefix': 'S01',        # Prefijo para los archivos generados
    'firma_celda': 'K96',        # ⚠️ CAMBIAR: Celda donde se insertará la firma
}

