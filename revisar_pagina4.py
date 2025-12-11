import re

# Leer archivos
with open('app/mapeos/zulia_mapping.py', 'r', encoding='utf-8') as f:
    mapping_lines = f.readlines()
    mapping_content = ''.join(mapping_lines)

with open('app/templates/subestacion/S_XX_ZULIA/s_xx_zulia.html', 'r', encoding='utf-8') as f:
    html_lines = f.readlines()
    html_content = ''.join(html_lines)

# Extraer IDs del mapping con sus líneas (PÁGINA 4: líneas 128-160 aproximadamente)
mapping_dict = {}
for i, line in enumerate(mapping_lines, 1):
    # Solo líneas de la página 4 (basado en comentarios)
    if i >= 128 and i <= 160:
        matches = re.findall(r'"([^"]+)"\s*:', line)
        for match in matches:
            if match not in ['mapping', 'template', 'excel_template', 'excel_sheet', 'file_prefix', 'firma_celda']:
                if match not in mapping_dict:
                    mapping_dict[match] = []
                mapping_dict[match].append(i)

# Extraer IDs del HTML de la página 4 (líneas 231-318 aproximadamente)
html_dict = {}
for i, line in enumerate(html_lines, 1):
    # Solo líneas de la página 4
    if i >= 231 and i <= 318:
        matches = re.findall(r'id="([^"]+)"', line)
        for match in matches:
            if match != 'planillaForm':
                if match not in html_dict:
                    html_dict[match] = []
                html_dict[match].append(i)

# Obtener todos los IDs únicos de la página 4
all_ids = sorted(set(mapping_dict.keys()) | set(html_dict.keys()))

# Crear tabla
print("=" * 180)
print("REVISION PAGINA 4: NIVEL 13.8kV - TRANSFORMADORES DE CORRIENTE Y TENSIÓN")
print("=" * 180)
print(f"{'NUM':<6} {'ID_MAPEO':<50} {'#FILA_MAPEO':<15} {'ID_HTML':<50} {'#FILA_HTML':<15} {'ESTADO':<15}")
print("=" * 180)

num = 1
for id_name in all_ids:
    # Columnas para mapping
    if id_name in mapping_dict:
        id_mapping_display = id_name[:48] + ".." if len(id_name) > 50 else id_name
        fila_mapping = ",".join(map(str, mapping_dict[id_name]))
    else:
        id_mapping_display = ""
        fila_mapping = ""
    
    # Columnas para HTML
    if id_name in html_dict:
        id_html_display = id_name[:48] + ".." if len(id_name) > 50 else id_name
        fila_html = ",".join(map(str, html_dict[id_name]))
    else:
        id_html_display = ""
        fila_html = ""
    
    # Determinar estado
    if id_name in mapping_dict and id_name in html_dict:
        estado = "COINCIDE"
    elif id_name in mapping_dict:
        estado = "SOLO MAPEO"
    else:
        estado = "SOLO HTML"
    
    print(f"{num:<6} {id_mapping_display:<50} {fila_mapping:<15} {id_html_display:<50} {fila_html:<15} {estado:<15}")
    num += 1

print("=" * 180)
print(f"\nRESUMEN PAGINA 4:")
print(f"  Total IDs encontrados: {len(all_ids)}")
print(f"  IDs que coinciden: {len([id for id in all_ids if id in mapping_dict and id in html_dict])}")
print(f"  IDs solo en mapping: {len([id for id in all_ids if id in mapping_dict and id not in html_dict])}")
print(f"  IDs solo en HTML: {len([id for id in all_ids if id not in mapping_dict and id in html_dict])}")

# Mostrar discrepancias
print("\n" + "=" * 180)
print("DISCREPANCIAS DETALLADAS:")
print("=" * 180)

solo_mapping = [id for id in all_ids if id in mapping_dict and id not in html_dict]
solo_html = [id for id in all_ids if id not in mapping_dict and id in html_dict]

if solo_mapping:
    print("\nIDs solo en MAPPING (necesitan agregarse al HTML o corregir nombre):")
    for id_name in solo_mapping:
        print(f"  - {id_name} (línea mapping: {','.join(map(str, mapping_dict[id_name]))})")

if solo_html:
    print("\nIDs solo en HTML (necesitan agregarse al mapping o corregir nombre):")
    for id_name in solo_html:
        print(f"  - {id_name} (línea HTML: {','.join(map(str, html_dict[id_name]))})")

if not solo_mapping and not solo_html:
    print("\n¡Perfecto! Todos los IDs de la PAGINA 4 coinciden.")

