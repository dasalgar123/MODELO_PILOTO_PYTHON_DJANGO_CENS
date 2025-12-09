import openpyxl
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import os
from django.conf import settings
import sys
import io

# Configurar UTF-8 para evitar errores de encoding en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Mapeo: Encabezado + PÁGINA 2
la_miel_mapping = {
    # Encabezado
    "fecha": "AN4",
    "ejecuto": "j5",
    "numero_ot": "J4",
    
    # PÁGINA 2: TRANSFORMADORES DE TENSIÓN Y DPS 34.5 KV
    "id_tt_fase_r_cdd": "AS10",
    "id_tt_fase_s_cdd": "BD10",
    "id_tt_fase_t_cdd": "BO10",

    "id_conectores_fase_a_tt": "J12",
    "id_conectores_fase_b_tt": "P12",
    "id_conectores_fase_c_tt": "V12",
    "id_conectores_ft_dps": "AN12",

    "id_porcelana_fase_a_tt": "J13",
    "id_porcelana_fase_b_tt": "P13",
    "id_porcelana_fase_c_tt": "V13",
    "id_porcelana_fase_ft_dps": "AB13",

    "id_Caja_agrupamiento_fase_a_tt": "J14",
    "id_Caja_agrupamiento_fase_b_tt": "P14",
    "id_Caja_agrupamiento_fase_c_tt": "V14",
    "id_Caja_agrupamiento_fase_ft_dps": "AB14",

    "id_Limpieza_fase_a_tt": "J15",
    "id_Limpieza_fase_b_tt": "P15",
    "id_Limpieza_fase_c_tt": "V15",
    "id_Limpieza_ft_dps": "AB15",

    "id_Cableado_fase_a_tt": "j16",
    "id_Cableado_fase_b_tt": "p16",
    "id_Cableado_fase_c_tt": "v16",
    "id_Cableado_fase_ft_dps": "aB16",

    "id_Puesta_tierra_fase_a_tt": "j17",
    "id_Puesta_tierra_fase_b_tt": "p17",
    "id_Puesta_tierra_fase_c_tt": "v17",
    "id_Puesta_tierra_ft_dps": "aB17",

    "observaciones_TT_Y_DPS": "aE13",
    
    # PÁGINA 3: SECCIONADORES ASOCIADOS 34.5 KV (SB11, SST12)
    "it_Estado_SB11": "J21",
    "it_Estado_SB12": "N21",
    "it_Conectores_SB11": "J22",
    "it_Conectores_SB12": "N22",
    "it_Porcelana_SB11": "J23",
    "it_Porcelana_SB12": "n23",
    "it_Mecanismo_SB11": "j24",
    "it_Mecanismo_SB12": "N24",
    "it_Accionamiento_SB11": "j25",
    "it_Accionamiento_SB12": "N25",

    "it_Estado_SB11": "aa21",
    "it_Estado_SB12": "ae21",
    "it_Gab_Control_SB11": "aa22",
    "it_Gab_Control_SB12": "ae22",
    "it_Aisladores_SB11": "aa23",
    "it_Aisladores_SB12": "ae23",
    "it_Puesta_tierra_SB11": "aa24",
    "it_Puesta_tierras_SB12": "ae24",
    "observaciones_3": "ai21"
}

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'daniel' and password == '88310462':
            return redirect('/app/main_menu/')
        else:
            return render(request, 'login/login.html', {'error_message': 'Usuario o contraseña incorrectos'})
    return render(request, 'login/login.html')

def main_menu(request):
    return render(request, 'menu/main_menu.html')

def la_miel_list(request):
    if request.method == 'POST':
        excel_template_path = "C:\\Users\\ANDRES\\Desktop\\la miel\\app\\templates\\EXEL\\PLT_201_MST_032_LA MIEL.xlsx"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_excel_file_name = f"{timestamp}_S30_LAMIEL.xlsx"
        excel_output_dir = os.path.join(settings.BASE_DIR, "EXCEL_GUARDADOS")
        os.makedirs(excel_output_dir, exist_ok=True)
        new_excel_file_path = os.path.join(excel_output_dir, new_excel_file_name)

        workbook = openpyxl.load_workbook(excel_template_path)
        workbook.save(new_excel_file_path)

        workbook = openpyxl.load_workbook(new_excel_file_path)
        sheet = workbook['PLT_201_MST_032_ACT']

        try:
            for field_name, cell_ref in la_miel_mapping.items():
                value = request.POST.get(field_name)
                if value:
                    try:
                        sheet[cell_ref] = value
                    except AttributeError:
                        # Celda combinada, se salta
                        continue
            
            workbook.save(new_excel_file_path)
            with open(new_excel_file_path, 'rb') as excel_file:
                response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={new_excel_file_name}'
                return response

        except Exception as e:
            return render(request, 'subestacion/S30_LA_MIEL/s30_la_miel.html', {'error_message': f'Error al guardar y descargar Excel: {str(e)}'})
    return render(request, 'subestacion/S30_LA_MIEL/s30_la_miel.html', {})
