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

    "observaciones_4": "am44",
    
    # PÁGINA 5: TRANSFORMADOR 34.5/13.8kV
    "it_Conductores_primarios tc34": "m36",
    "it_Conectores_tc34": "m37",
    "it_Bujes_primarios_tc34": "m38",
    "it_Bujes_secundarios_tc34": "m39",
    "it_Silica_gel_tc34": "m40",
    "it_Termómetro_del_aceite tc34": "m41",
    "it_Termómetro_devanado_tc34": "m42",
    "it_Conduct_secundarios_tc34": "m43",

    "it_Gabinete_de_control_tc34": "af36",
    "it_Breaker_tc34": "af37",
    "it_Bornera_tc34": "af38",
    "it_Cableado_tc34": "af39",
    "it_Iluminación_tc34": "af40",
    "it_Limpieza_tc34": "af41",
    "it_Mandos_tc34": "af42",
    "it_DPS_tc34": "af43",
    
    "FASE_R_PRIM_CD": "ar37",
    "FASE R SECUND_CD": "aw37",
    "FASE_S_PRIM_CD_tc34": "ar38",
    "FASE_S_SECUND_CD_tc34": "aw38",
    "FASE_T_PRIM_CD": "aw39",
    "FASE_T_SECUND_CD": "aw39",
    
    "it_Aceite_tc34": "am42",
    "it_AT_tc34": "ar42",
    "it_Bt_tc34": "aw42",

    "Estado_silica_gel_tc34": "bb37",
    "Color_actual_del_GEL_tc34": "bg38",
    "it_Posición_conmutador_tc34": "bb42",

    "80ºC_Max_tc34": "bs38",
    "25ºC_Max_tc34": "bs40",
    "20ºC_Max_tc34": "bs42",

    "OBSERVACIONES_5_tc34": "am44",
    
    # PÁGINA 6: INTERRUPTOR DE 13.8KV IT20
    "it_Conectores_i13": "k50",
    "it_Conductores_eléctr_i13": "k51",
    "it_Porcelana_i13": "k52",
    "it_Sistema_mecánico_i13": "k53",
    "it_Presión_de_SF6_i13": "k54",
    "it_Manómetros_i13": "k55",
    "it_Mangueras_presión_i13": "y50",
    "it_Estructura_metálica_i13": "y51",
    "it_Puesta_a_tierra_i13": "y52",
    "it_Gabinete_de_control_i13": "y53",
    "it_Borneras_i13": "y54",
    "it_Cableado_i13": "y55",
    "it_Breakers_i13": "ai50",
    "it_Iluminación_i13": "ai51",
    "it_DPS_i13": "ai52",
    "it_Mandos_i13": "ai53",
    "it_Calefacción_i13": "ai54",
    "it_Limpieza_i13": "ai55",
    "Presión_Nominal_psmi": "AW50",
    "Presión_Leída_psmi": "AW52",
    "Número Maniobras_interruptor_IT10_psmi": "AW54",
    "OBSERVACIONES_6": "BB50",
    
    # PÁGINA 7: SECCIONADORES ASOCIADOS 13.8 KV
    "it_Estado_sb21": "j59",
    "it_Conectores_sb21": "j60",
    "it_Porcelana_sb21": "j61",
    "it_Mecanismo_sb21": "w59",
    "it_Accionamiento_sb21": "w60",
    "it_Gab_De_Control_sb21": "w61",
    "it_Aisladores_sb21": "aj59",
    "it_Puesta a tierra_sb21": "aj60",
    "OBSERVACIONES_7_sb21": "an59",
    
    # PÁGINA 8: TRANSFORMADOR DE CORRIENTE-TRANSFORMADOR DE TENSIÓN
    "it_Conectores_fase_a_tc": "i64",
    "it_Porcelana_fase_a_tc": "i65",
    "it_Caja_de_agrups_fase_a_tc": "i66",
    "it_Limpieza_fase_a_tc": "i67",
    "it_Cableado_fase_a_tc": "i68",
    "it_Puesta_a_tierra_fase_a_tc": "i69",

    "it_Conectores_fase_b_tc": "n64",
    "it_Porcelana_fase_b_tc": "n65",
    "it_Caja_de_agrup_fase_c_tc": "n66",
    "it_Limpieza_fase_b_tc": "n67",
    "it_Cableado_c_tc": "n68",

    "it_Puesta_a_tierra_c_tc": "n69",
    "it_Conectores_fase_c_tc": "s64",
    "it_Porcelana_fase_c_tc": "s65",
    "it_Caja_de_agrup_fase_b_tc": "s66",
    "it_Limpieza_fase_c_tc": "s67",
    "it_Cableado_fase_b_tc": "s68",
    "it_Puesta_a_tierra_fase_b_tc": "s69",

    "it_Conectores_fase_a_tt": "af64",
    "it_Porcelana_fase_a_tt": "af65",
    "it_Limpieza_fase_a_tt": "af66",
    "it_Cableado_fase_a_tt": "af67",
    "it_Puesta_a_tierra_fase_a_tt": "af68",

    "it_Conectores_fase_b_tt": "ak64",
    "it_Porcelana_fase_b_tt": "ak65",
    "it_Limpieza_fase_b_tt": "ak66",
    "it_Cableado_fase_b_tt": "ak67",
    "it_Puesta_a_tierra_fase_b_tt": "ak68",
    
    "it_Conectores_fase_c_tt": "ap64",
    "it_Porcelana_fase_c_tt": "ap65",
    "it_Limpieza_fase_c_tt": "ap66",
    "it_Cableado_fase_c_tt": "ap67",
    "it_Puesta_a_tierra_fase_c_tt": "ap68",
    
    "OBSERVACIONES_8": "au64",
    
    # PÁGINA 9: RECONECTADORES SALIDA 13.8KV
    "it_Tanque_Reconectador_R267": "R71",
    "it_Conectores_y_bujes_de_entrada_R267": "R72",
    "it_Conectores_y_bujes_de_salida_R267": "R73",
    "it_Breaker_AC_Serv_Aux_R267": "R74",
    "it_DPS_salida_Reconectador_R267": "R75",
    "it_Sistema_de_puesta_a_tierra_R267": "R76",
    "it_Número_Operaciones_R267": "R77",

    "it_Tanque_Reconectador_RC0196": "W71",
    "it_TConectores_y_bujes_de_entrada_RC0196": "W72",
    "it_Conectores_y_bujes_de_salida_RC0196": "W73",
    "it_DPS_salida_Reconectador_RC0196": "W74",
    "it_Sistema_de_puesta_a_tierra_RC0196": "W75",
    "it_Número_Operaciones_RC0196": "W76",

    "it_Hermeticidad_control_R267": "AN71",
    "it_Breaker_AC_ServAux_RC0196": "AN72",
    "it_Breaker_Baterías_R267": "AN73",
    "it_DPSVaristor_R267": "AN74",
    "it_Limpieza_Gab_Control_R267": "AN75",
    "it_Estructura_Soporte_R267": "AN76",

    "it_Hermeticidad_control_RC0196": "AS71",
    "it_Breaker_AC_ServAux_RC0196": "AS72",
    "it_Breaker_Baterías_RC0196": "AS73",
    "it_DPS_Varistor_RC0196": "AS74",
    "it_Limpieza_Gab_Control_RC0196": "AS75",
    "it_Estructura_Soporte_RC0196": "AS76",
   
    "OBSERVACIONES_9": "AX70"
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
