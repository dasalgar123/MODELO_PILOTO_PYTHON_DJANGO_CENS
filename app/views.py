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
    "observaciones_3": "ai21",
    
    # PÁGINA 4: TRANSFORMADOR DE CORRIENTE E INTERRUPTOR 34.5KV IT10
    "it_conectores_tc34": "h28",
    "it_Porcelana_tc34": "h29",
    "it_Caja_de_agrupamiento_tc34": "h30",
    "it_Limpieza_tc34": "h31",
    "it_Cableado_tc34": "h32",
    "it_Puesta_tierra_tc34": "h33",

    "it_conectores i34": "x28",
    "it_Conductores_eléctr_i34": "x29",
    "it_Porcelana_i34": "x30",
    "it_Sistema_Mecánico_i34": "x31",
    "it_PresionSF6_i34": "x32",
    "it_Manometros_i34": "x33",

    "it_Mangueras_presión_i34": "am28",
    "it_Estructura_metálica_i34": "am29",
    "it_Puesta_a_Tierra_i34": "am30",
    "it_Gabinete_Control_i34": "am31",
    "it_Borneras_i34": "am32",
    "it_Cableado_i34": "am33",

    "it_Breakers_i34": "bb28",
    "it_Iluminación_i34": "bb29",
    "it_DPS_i34": "bb30",
    "it_Mandos_i34": "bb31",
    "it_Calefaccion_i34": "bb32",
    "it_Limpieza_i34": "bb33",
    "presion_sf6_4_i34": "bp28",
    "it_Presión_Leída_spmi34": "bp30",
    "it_Número_Maniobras_interruptor IT10_spmi34": "bp32",
    "observaciones_4": "am44"
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
        # DEBUG: Ver valores específicos
        limpieza = request.POST.get('it_Limpieza_tc34')
        cableado = request.POST.get('it_Cableado_tc34')
        print(f"DEBUG - Limpieza tc34: '{limpieza}'")
        print(f"DEBUG - Cableado tc34: '{cableado}'")
        
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
