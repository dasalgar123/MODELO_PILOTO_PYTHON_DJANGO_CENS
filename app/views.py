import openpyxl

from openpyxl.drawing.image import Image

from django.shortcuts import render, redirect

from django.http import HttpResponse

from datetime import datetime

import os

from django.conf import settings

import sys

import io

import tempfile
import time
import shutil
from PIL import Image as PILImage
from app.inspectores_config import obtener_nombre_inspector


# Configurar UTF-8 para evitar errores de encoding en Windows

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')



# ============================================================================
# ORGANIZACIÓN DE MAPEOS POR FORMULARIO
# ============================================================================
# Estructura escalable: cada formulario tiene su propio mapeo, template, Excel, etc.
# Para agregar un nuevo formulario, solo agrega una entrada aquí.

# Mapeo: Encabezado + PÁGINA 2 - FORMULARIO S30 LA MIEL
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

   

    "OBSERVACIONES_9": "AX70",

    

    # PÁGINA 10: SECCIONADOR MONOPOLAR 13.8 KV

    # Estado físico equipo - LA VEGA

    "it_Estado_físico_equipo-LV-FASE-A": "K80",

    "it_Estado_físico_equipo-LV-FASE-B": "N80",

    "it_Estado_físico_equipo-LV-FASE-C": "Q80",

    # Estado físico equipo - LAS CUADRAS

    "it_Estado_físico_equipo-LC-FASE-A": "T80",

    "it_Estado_físico_equipo-LC-FASE-B": "W80",

    "it_Estado_físico_equipo-LC-FASE-C": "Z80",

    # Estado físico equipo - SALOBRE

    "it_Estado_físico_equipo-S-FASE-A": "AC80",

    "it_Estado_físico_equipo-S-FASE-B": "AF80",

    "it_Estado_físico_equipo-S-FASE-C": "AI80",

    # Estado físico equipo - SANTA ROSA

    "it_Estado_físico_equipo-SR-FASE-A": "AL80",

    "it_Estado_físico_equipo-SR-FASE-B": "AO80",

    "it_Estado_físico_equipo-SR-FASE-C": "AR80",

    # Estado físico equipo - SERVICIOS AUX

    "it_Estado_físico_equipo-SA-FASE-A": "AU80",

    "it_Estado_físico_equipo-SA-FASE-B": "AX80",

    "it_Estado_físico_equipo-SA-FASE-C": "BA80",

    # Estado físico equipo - DPS

    "it_Estado_físico_equipo_SA": "BK80",

    "it_Estado_físico_equipor_ET": "BP80",

    

    # Aisladores - LA VEGA

    "it_Aisladores-LV-FASE-A": "K81",

    "it_Aisladores-LV-FASE-B": "N81",

    "it_Aisladores-LV-FASE-C": "Q81",

    # Aisladores - LAS CUADRAS

    "it_Aisladores-LC-FASE-A": "T81",

    "it_Aisladores-LC-FASE-B": "W81",

    "it_Aisladores-LC-FASE-C": "Z81",

    # Aisladores - SALOBRE

    "it_Aisladores-S-FASE-A": "AC81",

    "it_Aisladores-S-FASE-B": "AF81",

    "it_Aisladores-S-FASE-C": "AI81",

    # Aisladores - SANTA ROSA

    "it_Aisladores-SR-FASE-A": "AL81",

    "it_Aisladores-SR-FASE-B": "AO81",

    "it_Aisladores-SR-FASE-C": "AR81",

    # Aisladores - SERVICIOS AUX

    "it_Aisladores-SA-FASE-A": "AU81",

    "it_Aisladores-SA-FASE-B": "AX81",

    "it_Aisladores-SA-FASE-C": "BA81",

    # Aisladores - DPS

    "it_Aisladores_SA": "BK81",

    "it_Aisladores_ET": "BP81",

    

    # Conectores - LA VEGA

    "it_Conectores-LV-FASE-A": "K82",

    "it_Conectores-LV-FASE-B": "N82",

    "it_Conectores-LV-FASE-C": "Q82",

    # Conectores - LAS CUADRAS

     "it_Conectores-LC-FASE-A": "T82",

    "it_Conectores-LC-FASE-B": "W82",

    "it_Conectores-LC-FASE-C": "Z82",

    # Conectores - SALOBRE

    "it_Conectores-S-FASE-A": "AC82",

    "it_Conectores-S-FASE-B": "AF82",

    "it_Conectores-S-FASE-C": "AI82",

    # Conectores - SANTA ROSA

    "it_Conectores-SR-FASE-A": "AL82",

    "it_Conectores-SR-FASE-B": "AO82",

    "it_Conectores-SR-FASE-C": "AR82",

    # Conectores - SERVICIOS AUX

    "it_Conectores-SA-FASE-A": "AU82",

    "it_Conectores-SA-FASE-B": "AX82",

    "it_Conectores-SA-FASE-C": "BA82",

    # Conectores - DPS

    "it_Conectores_SB": "BK82",

    "it_Conectores_ET": "BP82",

    

    # Enganche - LA VEGA

    "it_Enganche-LV-FASE-A": "K83",

    "it_Enganche-LV-FASE-B": "N83",

    "it_Enganche-LV-FASE-C": "Q83",

    # Enganche - LAS CUADRAS

    "it_Enganche-LC-FASE-A": "T83",

    "it_Enganche-LC-FASE-B": "W83",

    "it_Enganche-LC-FASE-C": "Z83",

    # Enganche - SALOBRE

    "it_Enganche-S-FASE-A": "AC83",

    "it_Enganche-S-FASE-B": "AF83",

    "it_Enganche-S-FASE-C": "AI83",

    # Enganche - SANTA ROSA

    "it_Enganche-SR-FASE-A": "AL83",

    "it_Enganche-SR-FASE-B": "AO83",

    "it_Enganche-SR-FASE-C": "AR83",

    # Enganche - SERVICIOS AUX

    "it_Enganche-SA-FASE-A": "AU83",

    "it_Enganche-SA-FASE-B": "AX83",

    "it_Enganche-SA-FASE-C": "BA83",

    # Enganche - DPS

    "it_Conductor_SA": "BK83",

    "it_Conductor_ET": "BP83",

    

    # Conductor - LA VEGA

    "it_Conductor-lv-fase-a": "K84",

    "it_Conductor-lv-fase-b": "N84",

    "it_Conductor-lv-fase-c": "Q84",

    # Conductor - LAS CUADRAS

    "it_Conductor-lc-fase-a": "T84",

    "it_Conductor-lc-fase-b": "W84",

    "it_Conductor-lc-fase-c": "Z84",

    # Conductor - SALOBRE

    "it_Conductor-s-fase-a": "AC84",

    "it_Conductor-s-fase-b": "AF84",

    "it_Conductor-s-fase-c": "AI84",

    # Conductor - SANTA ROSA

    "it_Conductor-sr-fase-a": "AL84",

    "it_Conductor-sr-fase-b": "AO84",

    "it_Conductor-sr-fase-c": "AR84",

    # Conductor - SERVICIOS AUX

    "it_Conductor-sa-fase-a": "AU84",

    "it_Conductor-sa-fase-b": "AX84",

    "it_Conductor-SA-fase-c": "BA84",

    # Conductor - DPS

    "it_Conexión_SA": "BK84",

    "it_Conexión_ET": "BP84",

    

    "observaciones_10": "A87",

    

    # PÁGINA 11: INSTALACIONES/LOCATIVAS

    "Iluminación_Óptima_il": "N89",

    "Iluminación_Regular_il": "V89",

    "Candado_Óptima_il": "AP89",

    "Candado_Regular_il": "AX89",

    "Aseo_Óptima_il": "N90",

    "Aseo_Regular_il": "V90",

    "Av_Óptima_il": "AP90",

    "Av_Regular_il": "AX90",

    "Maleza_Óptima_il": "N91",

    "Maleza_Regular_il": "V91",

    "ZTV_Óptima_il": "AP91",

    "ZTV_Regular_il": "AX91",

    "Triturado_Óptima_il": "N92",

    "Triturado_Regular_il": "V92",

    "Canal_aguas_lluvias_Óptima_il": "AP92",

    "it_Canal_aguas_lluvias_Regular_RC0196_il": "AX92",

    "Encerramiento_Óptima_il": "N93",

    "Encerramiento_Regular_il": "V93",

    "Cámara_Vigilancia_Óptima_il": "AP93",

    "Cámara_Vigilancia_Regular_il": "AX93",

    "OBSERVACIONES_11": "BA89",
    
    # FIRMA DIGITAL (se inserta como imagen, no como texto)
    # El campo "firma_digital" del formulario se inserta como imagen en la celda K96
    # Ver: FORMULARIOS_CONFIG['s30_la_miel']['firma_celda'] = 'K96'
}

# ============================================================================
# CONFIGURACIÓN DE FORMULARIOS
# ============================================================================
# Importar configuraciones de formularios desde carpeta mapeos
try:
    from app.mapeos.s01_mapping import s01_mapping, S01_CONFIG
except ImportError:
    s01_mapping = {}
    S01_CONFIG = {}

# Diccionario principal que organiza todos los formularios
FORMULARIOS_CONFIG = {
    's30_la_miel': {
        'mapping': la_miel_mapping,
        'template': 'subestacion/S30_LA_MIEL/s30_la_miel.html',
        'excel_template': 'C:\\Users\\ANDRES\\Desktop\\la miel\\app\\templates\\EXEL\\PLT_201_MST_032_LA MIEL.xlsx',
        'excel_sheet': 'PLT_201_MST_032_ACT',
        'file_prefix': 'S30_LAMIEL',
        'firma_celda': 'K96',
    },
    's01': S01_CONFIG,
}



def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        

        if username == 'daniel' and password == '88310462':

            # Guardar el nombre del inspector en la sesión
            request.session['inspector_username'] = username
            request.session['inspector_nombre'] = 'Daniel Salinas'  # Mapeo de usuario a nombre
            return redirect('/app/main_menu/')

        else:

            return render(request, 'componetes/login/login.html', {'error_message': 'Usuario o contraseña incorrectos'})

    return render(request, 'componetes/login/login.html')



def main_menu(request):

    return render(request, 'componetes/menu/main_menu.html')



# ============================================================================
# FUNCIÓN GENÉRICA PARA PROCESAR FORMULARIOS
# ============================================================================
def procesar_formulario(request, formulario_id):
    """
    Función genérica que procesa cualquier formulario basándose en la configuración.
    Esta función es escalable para los 42 formularios.
    
    Args:
        request: HttpRequest de Django
        formulario_id: ID del formulario (ej: 's30_la_miel', 's01', etc.)
    
    Returns:
        HttpResponse con el Excel generado o render del template
    """
    # Validar que el formulario existe en la configuración
    if formulario_id not in FORMULARIOS_CONFIG:
        return HttpResponse(f'Error: Formulario "{formulario_id}" no encontrado en la configuración.', status=404)
    
    config = FORMULARIOS_CONFIG[formulario_id]
    mapping = config['mapping']
    template = config['template']
    excel_template_path = config['excel_template']
    excel_sheet_name = config['excel_sheet']
    file_prefix = config['file_prefix']
    firma_celda = config['firma_celda']
    
    if request.method == 'POST':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_excel_file_name = f"{timestamp}_{file_prefix}.xlsx"

        # Verificar que el template Excel existe
        if not os.path.exists(excel_template_path):
            return render(request, template, {'error_message': f'Error: No se encontró el archivo Excel template en: {excel_template_path}'})

        # Crear archivo temporal
        temp_excel = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
        temp_excel_path = temp_excel.name
        temp_excel.close()

        try:
            # Cargar workbook desde template
            workbook = openpyxl.load_workbook(excel_template_path)
            
            # Verificar que la hoja existe
            if excel_sheet_name not in workbook.sheetnames:
                workbook.close()
                return render(request, template, {'error_message': f'Error: No se encontró la hoja "{excel_sheet_name}" en el Excel.'})
            
            sheet = workbook[excel_sheet_name]

            try:
                # Guardar todos los campos según el mapeo
                guardados = 0
                errores = 0
                campos_no_guardados = []
                
                for field_name, cell_ref in mapping.items():
                    if field_name in request.POST:
                        value = request.POST.get(field_name)
                        try:
                            cell = sheet[cell_ref]
                            cell.value = value
                            guardados += 1
                        except (AttributeError, ValueError, KeyError, Exception) as e:
                            campos_no_guardados.append(f"{field_name} ({cell_ref}): {type(e).__name__}: {e}")
                            errores += 1
                    else:
                        campos_no_guardados.append(f"{field_name} ({cell_ref}): NO ENVIADO EN POST")
                
                print(f"\n[{formulario_id}] Total guardados: {guardados}, Errores: {errores}")
                if campos_no_guardados:
                    print(f"\n⚠️ CAMPOS NO GUARDADOS ({len(campos_no_guardados)}):")
                    for campo in campos_no_guardados[:10]:  # Mostrar solo los primeros 10
                        print(f"  - {campo}")
                
                # Insertar firma digital directamente en Excel
                temp_firma_path = None
                firma_insertada = False
                if 'firma_digital' in request.FILES:
                    firma = request.FILES['firma_digital']
                    
                    try:
                        # Guardar imagen en memoria primero para validar
                        imagen_bytes = b''
                        for chunk in firma.chunks():
                            imagen_bytes += chunk
                        
                        if len(imagen_bytes) == 0:
                            print(f"❌ Error: La imagen de firma está vacía")
                        else:
                            # Validar y detectar formato usando PIL
                            try:
                                pil_img = PILImage.open(io.BytesIO(imagen_bytes))
                                # Detectar formato real
                                formato_original = pil_img.format.lower() if pil_img.format else 'png'
                                print(f"📸 Formato de imagen detectado: {formato_original}")
                                
                                # Formatos compatibles con Excel: png, jpeg, gif
                                formatos_compatibles = ['png', 'jpeg', 'jpg', 'gif']
                                
                                # Si el formato no es compatible, convertir a PNG
                                if formato_original not in formatos_compatibles:
                                    print(f"⚠️ Formato {formato_original} no compatible, convirtiendo a PNG")
                                    formato_original = 'png'
                                    # Convertir a RGB si tiene transparencia (modo RGBA)
                                    if pil_img.mode in ('RGBA', 'LA', 'P'):
                                        fondo = PILImage.new('RGB', pil_img.size, (255, 255, 255))
                                        if pil_img.mode == 'P':
                                            pil_img = pil_img.convert('RGBA')
                                        fondo.paste(pil_img, mask=pil_img.split()[-1] if pil_img.mode in ('RGBA', 'LA') else None)
                                        pil_img = fondo
                                    elif pil_img.mode != 'RGB':
                                        pil_img = pil_img.convert('RGB')
                                
                                # Guardar imagen procesada en archivo temporal con extensión correcta
                                extension = '.png' if formato_original == 'png' else ('.jpg' if formato_original in ('jpeg', 'jpg') else '.gif')
                                temp_firma = tempfile.NamedTemporaryFile(delete=False, suffix=extension)
                                temp_firma_path = temp_firma.name
                                temp_firma.close()
                                
                                # Guardar imagen procesada
                                pil_img.save(temp_firma_path, format=formato_original.upper())
                                pil_img.close()
                                
                                # Verificar que el archivo se guardó correctamente
                                if os.path.exists(temp_firma_path) and os.path.getsize(temp_firma_path) > 0:
                                    # Crear objeto Image de openpyxl desde archivo
                                    img = Image(temp_firma_path)
                                    # Ajustar tamaño de la imagen
                                    img.width = 150
                                    img.height = 60
                                    # Insertar imagen en la celda especificada (K96 para s30_la_miel)
                                    sheet.add_image(img, firma_celda)
                                    firma_insertada = True
                                    print(f"✅ Firma insertada correctamente en celda {firma_celda}")
                                else:
                                    print(f"❌ Error: El archivo de firma no se guardó correctamente")
                                    
                            except Exception as e_img:
                                print(f"❌ Error al procesar imagen: {e_img}")
                                import traceback
                                traceback.print_exc()
                        
                    except Exception as e:
                        print(f"❌ Error al insertar firma en Excel: {e}")
                        import traceback
                        traceback.print_exc()
                else:
                    print(f"⚠️ No se subió firma digital")
                
                # Guardar Excel primero en archivo temporal (para evitar corrupción)
                workbook.save(temp_excel_path)
                workbook.close()  # Cerrar workbook para liberar el archivo en Windows
                
                # Limpiar archivo temporal de firma después de guardar el Excel
                if 'temp_firma_path' in locals() and os.path.exists(temp_firma_path):
                    try:
                        time.sleep(0.2)
                        os.unlink(temp_firma_path)
                    except:
                        pass
                
                # Esperar un momento para que Windows libere el archivo
                time.sleep(0.2)
                
                # Copiar archivo temporal a carpeta EXCEL_GUARDADOS
                excel_guardados_dir = os.path.join(settings.BASE_DIR, 'EXCEL_GUARDADOS')
                os.makedirs(excel_guardados_dir, exist_ok=True)
                excel_final_path = os.path.join(excel_guardados_dir, new_excel_file_name)
                shutil.copy2(temp_excel_path, excel_final_path)
                
                # Limpiar archivo temporal después de copiar
                if os.path.exists(temp_excel_path):
                    try:
                        time.sleep(0.1)
                        os.unlink(temp_excel_path)
                    except:
                        pass
                
                # Leer Excel en memoria para descarga desde el archivo final
                with open(excel_final_path, 'rb') as f:
                    excel_bytes = f.read()
                
                # Mensaje de éxito con ruta y estado de la firma
                mensaje_firma = ""
                if firma_insertada:
                    mensaje_firma = f"<br>✅ <strong>Firma guardada en celda {firma_celda}</strong>"
                elif 'firma_digital' not in request.FILES:
                    mensaje_firma = f"<br>⚠️ No se subió firma digital"
                
                mensaje_exito = f'<div style="background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; padding: 15px; margin: 10px 0; border-radius: 5px; font-size: 16px;">✅ Excel guardado correctamente en: {excel_final_path}{mensaje_firma}</div>'
                request.session['mensaje_exito'] = mensaje_exito
                
                # Si hay campos no guardados, agregar mensaje a la sesión
                if campos_no_guardados:
                    mensaje_error_html = f'<div style="background-color: #fff3cd; border: 2px solid #ffc107; padding: 15px; margin: 20px 0; border-radius: 5px;"><h3 style="color: #856404; margin-top: 0;">⚠️ CAMPOS NO GUARDADOS ({len(campos_no_guardados)}):</h3><ul style="margin: 10px 0; padding-left: 20px;">'
                    for campo in campos_no_guardados[:20]:  # Mostrar solo los primeros 20
                        mensaje_error_html += f'<li style="color: #dc3545; font-size: 8pt; font-weight: bold;">{campo}</li>'
                    mensaje_error_html += '</ul></div>'
                    request.session['error_message_html'] = mensaje_error_html
                
                # Preparar respuesta con Excel para descarga
                response = HttpResponse(excel_bytes, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename="{new_excel_file_name}"'
                response['Content-Length'] = len(excel_bytes)
                
                return response

            except Exception as e:
                # Limpiar archivos temporales en caso de error
                if 'workbook' in locals():
                    try:
                        workbook.close()
                    except:
                        pass
                if 'temp_excel_path' in locals() and os.path.exists(temp_excel_path):
                    try:
                        time.sleep(0.1)
                        os.unlink(temp_excel_path)
                    except:
                        pass
                return render(request, template, {'error_message': f'Error al procesar formulario: {str(e)}'})
        
        except Exception as e:
            # Limpiar archivos temporales en caso de error al cargar Excel
            if 'workbook' in locals():
                try:
                    workbook.close()
                except:
                    pass
            if 'temp_excel_path' in locals() and os.path.exists(temp_excel_path):
                try:
                    time.sleep(0.1)
                    os.unlink(temp_excel_path)
                except:
                    pass
            return render(request, template, {'error_message': f'Error al cargar Excel: {str(e)}'})
    
    # GET: Mostrar formulario
    error_message_html = request.session.pop('error_message_html', None)

    mensaje_exito = request.session.pop('mensaje_exito', None)
    return render(request, template, {
        'error_message_html': error_message_html,
        'mensaje_exito': mensaje_exito
    })

# ============================================================================
# VISTAS ESPECÍFICAS DE FORMULARIOS
# ============================================================================
# Estas vistas llaman a la función genérica procesar_formulario()
# Para agregar un nuevo formulario, solo crea una función vista y agrega la URL

def la_miel_list(request):
    """Vista específica para el formulario S30 LA MIEL"""
    return procesar_formulario(request, 's30_la_miel')

def s01_list(request):
    """Vista específica para el formulario S01"""
    return procesar_formulario(request, 's01')
