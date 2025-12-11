import re

# Leer archivos
with open('app/mapeos/zulia_mapping.py', 'r', encoding='utf-8') as f:
    mapping_lines = f.readlines()
    mapping_content = ''.join(mapping_lines)

with open('app/templates/subestacion/S_XX_ZULIA/s_xx_zulia.html', 'r', encoding='utf-8') as f:
    html_lines = f.readlines()
    html_content = ''.join(html_lines)

# Extraer IDs del mapping con sus líneas
mapping_dict = {}
for i, line in enumerate(mapping_lines, 1):
    matches = re.findall(r'"([^"]+)"\s*:', line)
    for match in matches:
        if match not in ['mapping', 'template', 'excel_template', 'excel_sheet', 'file_prefix', 'firma_celda']:
            if match not in mapping_dict:
                mapping_dict[match] = []
            mapping_dict[match].append(i)

# Extraer IDs del HTML con sus líneas
html_dict = {}
for i, line in enumerate(html_lines, 1):
    matches = re.findall(r'id="([^"]+)"', line)
    for match in matches:
        if match != 'planillaForm':
            if match not in html_dict:
                html_dict[match] = []
            html_dict[match].append(i)

# Obtener todos los IDs únicos ordenados
all_ids = sorted(set(mapping_dict.keys()) | set(html_dict.keys()))

# Crear tabla con formato solicitado
print("=" * 180)
print("TABLA COMPARATIVA DE IDs - FORMATO 7 COLUMNAS")
print("=" * 180)
print(f"{'NUM':<6} {'ID_MAPEO':<45} {'ID':<45} {'#FILA':<12} {'ID_HTML':<45} {'ID':<45} {'#FILA':<12}")
print("=" * 180)

num = 1
for id_name in all_ids:
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
    id_mapping_col3 = ""  # Dejar vacío, el ID ya está en columna 2
    id_html_col5 = id_html_display
    id_html_col6 = ""  # Dejar vacío, el ID ya está en columna 5
    
    print(f"{num:<6} {id_mapping_col2:<45} {id_mapping_col3:<45} {fila_mapping:<12} {id_html_col5:<45} {id_html_col6:<45} {fila_html:<12}")
    num += 1

print("=" * 180)
print(f"\nRESUMEN:")
print(f"  Total IDs unicos: {len(all_ids)}")
print(f"  IDs que coinciden: {len([id for id in all_ids if id in mapping_dict and id in html_dict])}")
print(f"  IDs solo en mapping: {len([id for id in all_ids if id in mapping_dict and id not in html_dict])}")
print(f"  IDs solo en HTML: {len([id for id in all_ids if id not in mapping_dict and id in html_dict])}")

