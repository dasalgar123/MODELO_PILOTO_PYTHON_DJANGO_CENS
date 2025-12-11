import re

# Leer archivos
with open('app/mapeos/zulia_mapping.py', 'r', encoding='utf-8') as f:
    mapping_lines = f.readlines()
    mapping_content = ''.join(mapping_lines)

with open('app/templates/subestacion/S_XX_ZULIA/encabezado/encabezado.html', 'r', encoding='utf-8') as f:
    encabezado_lines = f.readlines()
    encabezado_content = ''.join(encabezado_lines)

# IDs de la PÁGINA 1 (encabezado)
ids_pagina1 = ['fecha', 'ejecuto', 'numero_ot']

# Extraer IDs del mapping con sus líneas
mapping_dict = {}
for i, line in enumerate(mapping_lines, 1):
    matches = re.findall(r'"([^"]+)"\s*:', line)
    for match in matches:
        if match not in ['mapping', 'template', 'excel_template', 'excel_sheet', 'file_prefix', 'firma_celda']:
            if match not in mapping_dict:
                mapping_dict[match] = []
            mapping_dict[match].append(i)

# Extraer IDs del HTML del encabezado con sus líneas
html_dict = {}
for i, line in enumerate(encabezado_lines, 1):
    matches = re.findall(r'id="([^"]+)"', line)
    for match in matches:
        if match not in html_dict:
            html_dict[match] = []
        html_dict[match].append(i)

# Crear tabla solo para PÁGINA 1
print("=" * 180)
print("REVISION PÁGINA 1: DATOS GENERALES (ENCABEZADO)")
print("=" * 180)
print(f"{'NUM':<6} {'ID_MAPEO':<45} {'ID':<45} {'#FILA_MAPEO':<15} {'ID_HTML':<45} {'ID':<45} {'#FILA_HTML':<15}")
print("=" * 180)

num = 1
for id_name in ids_pagina1:
    # Columnas para mapping
    if id_name in mapping_dict:
        id_mapping_display = id_name[:43] + ".." if len(id_name) > 45 else id_name
        fila_mapping = ",".join(map(str, mapping_dict[id_name]))
    else:
        id_mapping_display = ""
        fila_mapping = ""
    
    # Columnas para HTML
    if id_name in html_dict:
        id_html_display = id_name[:43] + ".." if len(id_name) > 45 else id_name
        fila_html = ",".join(map(str, html_dict[id_name]))
    else:
        id_html_display = ""
        fila_html = ""
    
    # Mostrar ID solo una vez en cada lado
    id_mapping_col2 = id_mapping_display
    id_mapping_col3 = ""  # Dejar vacío
    id_html_col5 = id_html_display
    id_html_col6 = ""  # Dejar vacío
    
    # Determinar estado
    if id_name in mapping_dict and id_name in html_dict:
        estado = "COINCIDE"
    elif id_name in mapping_dict:
        estado = "SOLO MAPEO"
    else:
        estado = "SOLO HTML"
    
    print(f"{num:<6} {id_mapping_col2:<45} {id_mapping_col3:<45} {fila_mapping:<15} {id_html_col5:<45} {id_html_col6:<45} {fila_html:<15} {estado}")
    num += 1

print("=" * 180)
print(f"\nRESUMEN PÁGINA 1:")
print(f"  Total IDs esperados: {len(ids_pagina1)}")
print(f"  IDs que coinciden: {len([id for id in ids_pagina1 if id in mapping_dict and id in html_dict])}")
print(f"  IDs solo en mapping: {len([id for id in ids_pagina1 if id in mapping_dict and id not in html_dict])}")
print(f"  IDs solo en HTML: {len([id for id in ids_pagina1 if id not in mapping_dict and id in html_dict])}")

print("\n" + "=" * 180)
print("DETALLES:")
print("=" * 180)
for id_name in ids_pagina1:
    if id_name in mapping_dict:
        print(f"  {id_name}: En mapping línea(s) {','.join(map(str, mapping_dict[id_name]))}")
    else:
        print(f"  {id_name}: NO está en mapping")
    
    if id_name in html_dict:
        print(f"  {id_name}: En HTML línea(s) {','.join(map(str, html_dict[id_name]))}")
    else:
        print(f"  {id_name}: NO está en HTML")
    print()

