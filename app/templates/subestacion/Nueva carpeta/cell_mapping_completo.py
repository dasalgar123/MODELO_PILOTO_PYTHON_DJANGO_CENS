"""
Mapeo completo de IDs del formulario S30 LA MIEL a celdas Excel
Total: 332 elementos
Archivo: PLT_201_MST_032_LA MIEL.xlsx
"""

# ============================================================================
# PÁGINA 1: Datos generales
# ============================================================================
cell_mapping = {
    # Datos generales
    "planillaForm": "",
    "fecha": "AN4",
    "ejecuto": "j5",
    "numero ot ": "J4",
    
    # ============================================================================
    # PÁGINA 2: TRANSFORMADORES DE TENSIÓN Y DPS 34.5 KV
    # ============================================================================  
    # Transformadores de Tensión - Fases
    "id_tt_fase_r_cdd": "AS10",
    "id_tt_fase_s_cdd": "BD10",
    "id_tt_fase_t_cdd": "BQ10",
    
    # Conectores
    "id_conectores_fase_a_tt": "J12",
    "id_conectores_fase_b_tt": "P12",
    "id_conectores_fase_c_tt": "V12",
    "id_conectores_ft_dps": "AN12",
    
    # Porcelana
    "id_porcelana_fase_a_tt": "J13",
    "id_porcelana_fase_b_tt": "P13",
    "id_porcelana_fase_c_tt": "V13",
    "id_porcelana_fase_ft_dps": "AN13",
    
    # Caja de agrupamiento
    "id_Caja_agrupamiento_fase_a_tt": "J14",
    "id_Caja_agrupamiento_fase_b_tt": "P14",
    "id_Caja_agrupamiento_fase_c_tt": "V14",
    "id_Caja_agrupamiento_fase_ft_dps": "AN14",
    
    # Limpieza
    "id_Limpieza_fase_a_tt": "J15",
    "id_Limpieza_fase_b_tt": "P15",
    "id_Limpieza_fase_c_tt": "V15",
    "id_Limpieza_ft_dps": "AN15",
    
    # Cableado
    "id_Cableado_fase_a_tt": "j16",
    "id_Cableado_fase_b_tt": "p16",
    "id_Cableado_fase_c_tt": "v16",
    "id_Cableado_fase_ft_dps": "an16",
    
    # Puesta a tierra
    "id_Puesta_tierra_fase_a_tt": "j17",
    "id_Puesta_tierra_fase_b_tt": "p17",
    "id_Puesta_tierra_fase_c_tt": "v17",
    "id_Puesta_tierra_ft_dps": "an17",



    
    "observaciones_TT_Y_DPS": "an10",
    
    # ============================================================================
    # PÁGINA 3: SECCIONADORES ASOCIADOS 34.5 KV (SB11, SST12)
    # ============================================================================
    "it_Estado_SB11": "J21",            "it_Estado_SB12": "N21",
    "it_Conectores_SB11": "J22",        "it_Conectores_SB12": "N22",
    "it_Porcelana_SB11": "J23",         "it_Porcelana_SB12": "M23", 
    "it_Mecanismo_SB11": "j24",         "it_Mecanismo_SB12": "N24",
    "it_Gab_Control_SB11": "j25",       "it_Gab_Control_SB12": "N25",
    "it_Aisladores_SB11": "j26",        "it_Aisladores_SB12": "N26",
    "it_Puesta_tierra_SB11": "j27",     "it_Puesta_tierras_SB12": "N27",
    
    "observaciones_3": "ae21",
    
    # ============================================================================
    # PÁGINA 4: TRANSFORMADOR DE CORRIENTE E INTERRUPTOR 34.5KV IT10
    # ============================================================================
    "it_conectores_tc34": "h28",
    "it_Porcelana_tc34": "h29",
    "it_Caja_de_agrupamiento_tc34": "h30",
    "it_Limpieza_tc34": "h31",
    "it_Cableado_tc34": "h32",
    "it_Puesta_a_tierra_tc34": "h33",
           
    "it_conectores_i34": "x28",
    "it_Conductore_seléctr_i34": "x29",
    "it_Porcelana_i34": "x30",
    "it_Sistema_Mecánico_i34": "x31",
    "it_presion_sf6_4_i34": "x32",
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
    "Presión_Leída_spmi34": "bp30",
    "Número_Maniobras_interruptor_IT10_spmi34": "bp32",
    
    "observaciones_4": "am44",
         
    # ============================================================================
    # PÁGINA 5: TRANSFORMADOR 34.5/13.8kV-Contador de descargas-Estado silica gel-Nivel de aceite
    # ============================================================================     
    "it_Conductores_primarios_tc34": "m36",
    "it_Conectores_tc34": "m37",
    "it_Bujes_primarios_tc34": "m38",
    "it_Bujes_secundarios_tc34": "m39",
    "it_Silica_gel_tc34": "m40",
    "it_Termómetro_del_aceite_tc34": "m41",
    "it_Termómetro_devanado_tc34": "m42",
    "it_Conduct_secundarios_tc34": "m43",
     
    "it_Gabinete_de_control_tc34": "af36",
    "it_Breaker_tc34": "af37",
    "it_Bornera_tc34": "af38",
    "it_Cableado_tc34": "af39",
    "it_Iluminación_tc34": "af40",
    "it_Limpieza_tc34": "af41",
    "it_Mandos_tc34": "af42",
    "it_DPS_tc342": "af43",
      
    "FASE_R_PRIM_CD": "ar37",
    "FASE_R_SECUND_CD": "aw37",
        
    "FASE_S_PRIM_CD_tc34": "ar38",
    "FASE_S_SECUND_CD_tc34": "aw38",
       
    "FASE_T_PRIM_CD": "aw39",
    "FASE_T_SECUND_CD": "aw39",
    
    "it_Aceite_tc34": "am42",
    "it_AT_tc34": "ar42",
    "it_BT_tc34": "aw42",
      
    "it_Estado_silica_gel_tc34": "bb37",
    "Color_actual_del_GEL_tc34": "bg38",
    "Posición_conmutador_tc34": "bb42",
         
    "80ºC_Max_tc34": "bs38",
    "25ºC_Max_tc34": "bs40",
    "20ºC_Max_tc34": "bs42",
      
    "OBSERVACIONES_5_tc34": "am44",
         
      
    # ============================================================================
    # PÁGINA 6: INTERRUPTOR DE 13.8KV IT20
    # ============================================================================
    "it_Conectores_i13": "k50",
    "it_Conductores_eléctr_i13": "k51",
    "it_Porcelana_i13": "k52",
    "it_Sistema_mecánico_i132": "k53",
    "it_Presión_de_SF6_i13": "k54",
    "it_Manómetros_i13": "k55",
        
    "it_Mangueras_presión_i13": "y50 ",
    "it_Estructura_metálica_i13": "y51 ",
    "it_Puesta_a_tierra_i13": "y52",
    "it_Gabinete_de_control_i13": "y53 ",
    "it_Borneras_i13": "y54",
    "it_Cableado_i13": "y55 ",
    
    "it_Breakers_i13": "ai50",
    "it_Iluminación_i13": "ai51",
    "it_DPS_i13": "ai52",
    "it_Mandos_i13": "ai53",
    "it_Calefacción_i13": "ai54",
    "it_Limpieza_i13": "ai55",
          
    "Presión_Nominal_psmi": "AW50",
    "Presión_Leída_psmi": "AW52",
    "Número_Maniobras_interruptor_IT10_psmi": "AW54",
        
    "OBSERVACIONES_6": "BB50",
        
    # ============================================================================
    # PÁGINA 7:  SECCIONADORES ASOCIADOS 13.8  KV
    # ============================================================================
    "it_Estado_sb21": "j59",
    "it_Conectores_sb21": "j60",
    "it_Porcelana_sb21": "j61",
        
    it_Mecanismo_sb21": "w59",
    it_Accionamiento_sb21": "w59",
    it_Gab_De_Control_sb21": "w59",
    
    "it_Aisladores_sb21": "aj59",
    "it_Puesta a tierra_sb21": "aj60",
        
    "OBSERVACIONES_7_sb21": "an59",
        
    # ============================================================================
    # PÁGINA 8:TRANSFORMADOR DE CORRIENTE-TRANSFORMADOR DE TENSIÓN-OBSERVACIONES:
    # ============================================================================
    "it_Conectores_fase_a_tc": "i64",
    "it_Porcelana_fase_a_tc": "i65",
    "it_Caja_de_agrups_fase_a_tc: "i66",
    "it_Limpieza_fase_a_tc: "i67",
    "it_Cableado_fase_a_tc: "i68",
    "it_Puesta_a_tierra_fase_a_tc": "i69",
     
    "it_Conectores_fase_b_tc": "n64",
    "it_Porcelana_fase_b_tc": "n65",
    "it_Caja_de_agrup_fase_c_tc": "n66",
    "it_Limpieza_fase_b_tc": "n67",
    "it_Cableado_c_tc": "n68",
    "it_Puesta_a_tierra_c_tc": "n69",
    
    "it_Conectores_fase_c_tc": "s64",
    "it_Porcelana_fase_c_tc": "s65",
    "it_Caja de agrup_fase_b_tc": "s66",
    "it_Limpieza_fase_c_tc: "s67",
    "it_Cableado_fase_b_tc": "s68",
    "it_Puesta_a_tierra_fase_b_tc": "s69",
    
    "it_Conectores_fase_a_tt": "af64",
    "it_Porcelana_fase_a_tt": "af65",
    "it_Limpieza_fase_a_tt: "af66",
    "it_Cableado_fase_a_tt": "af67",
    "it_Puesta_a_tierra_fase_a_tt": "af68",
    
    "it_Conectores_fase_b_tt": "ak64",
    "it_Porcelana_fase_b_tt": "ak65",
    "it_Limpieza_fase_b_tt: "ak66",
    "it_Cableado_fase_b_tt": "ak67",
    "it_Puesta_a_tierra_fase_b_tt": "ak68",
    
    "it_Conectores_fase_c_tt": "ap64",
    "it_Porcelana_fase_c_tt": "ap65",
    "it_Limpieza_fase_c_tt: "ap66",
    "it_Cableado_fase_c_tt": "ap67",
    "it_Puesta_a_tierra_fase_c_tt": "ap68",
    
    "OBSERVACIONES_8": "au64",
    # ============================================================================
    # PÁGINA 9: RECONECTADORES SALIDA 13.8KV
    # ============================================================================
       
    "it_Tanque_Reconectador_R267": "r72",
    "it_Conectores_y_bujes_de_entrada_R267": "r73",
    "it_Conectores_y bujes_de_salida_R267": "r74",
    "it_DPS_Varistor_R267": "r75",
    "it_Sistema_de_puesta_a_tierra_R267": "r76",
    "it_Número_Operaciones_RC0196": "r77",
    
    "it_Tanque_Reconectador_RC0196": "w72",
    "it_Conectores_y_bujes_de_entrada_RC0196": "w73",
    "it_Conectores_y_bujes_de_salida_RC0196": "w74",
    "it_DPS_salida_Reconectador_RC0196": "w75",
    "it_Sistema_de_puesta_a_tierra_RC0196": "w76",
    "it_Número_Operaciones_R267": "w77",
    
    
    "it_Hermeticidad_control__R267": "an72",
    "it_Breaker AC_Serv_Aux_R267": "an73",
    "it_Breaker_Baterías_R267": "an74",
    "it_DPS_Varistor_R267": "an75",
    "it_Estructura_Soporte_R267": "an76",
    "it_Limpieza_Gab_Control_R267": "an77",
    
    
    "it_Hermeticidad_control_RC0196": "as72",
    "it_Breaker AC_Serv_Aux_RC0196": "as72",
    "it_Breaker_Baterías_RC0196": "as72",
    "it_DPS_Varistor_RC0196": "an75",
    "it_Estructura_Soporte_RC0196": "as72",
    "it_Limpieza_Gab_Control_RC0196": "as72",
    
    "OBSERVACIONES_9": "ax71"
     
    # ============================================================================
    # PÁGINA 10: SECCIONADOR MONOPOLAR 13.8 KV
    # ============================================================================
    "it_Estado_físico_equipo-LV-FASE-A": "k81",
    "id_Aisladores-LV-FASE-A": "k82",
    "id_Conectores-LV-FASE-A": "k83",
    "id_Enganche-LV-FASE-A": "k84",
    "id_Conductor-lv-fase-a": "k85",
    
    "id_Tanque Reconectador-LV-FASE-B": "n81",
    "id_Aisladores-LV-FASE-B": "n82",
    "id_Conectores-LV-FASE-B": "n83",
    "id_Enganche-LV-FASE-B": "n84",
    "id_Conductor-lv-fase-b": "n85",
    
    "id_Tanque Reconectador-LV-FASE-C": "q81",
    "id_Aisladores-LV-FASE-C": "q82",
    "id_Conectores-LV-FASE-C": "q83",
    "id_Enganche-LV-FASE-C": "q84",
    "id_Conductor-lv-fase-c": "q85",
    
    "id_Tanque Reconectador-LC-FASE-A": "t81",
    "id_Aisladores-LC-FASE-A": "t82",
    
    "id_Enganche-LC-FASE-A": "t84",
    "id_Conductor-lc-fase-a": "t85",
    
    "id_Tanque Reconectador-LC-FASE-B": "w81",
    "id_Aisladores-LC-FASE-B": "w82",
    "id_Conectores-LC-FASE-B": "w83",
    "id_Enganche-LC-FASE-B": "w84",
    "id_Conductor-lc-fase-b": "w85",
    
    "id_Tanque Reconectador-LC-FASE-C": "z81",
    "id_Aisladores-LC-FASE-C": "z82",
    "id_Conectores-LC-FASE-C": "z83",
    "id_Enganche-LC-FASE-C": "z84",
    "id_Conductor-lc-fase-c": "z85",
    
    "id_Tanque Reconectador-S-FASE-A": "ac81",
    "id_Aisladores-S-FASE-A": "ac82",
    "id_Conectores-S-FASE-A": "ac83",
    "id_Enganche-S-FASE-A": "ac84",
    "id_Conductor-s-fase-a": "ac85",
    
    "id_Tanque Reconectador-S-FASE-B": "af81",
    "id_Aisladores-S-FASE-B": "af82",
    "id_Conectores-S-FASE-B": "af83",
    "id_Enganche-S-FASE-B": "af84",
    "id_Conductor-s-fase-b": "af85",
    
    "id_Tanque Reconectador-S-FASE-C": "ai81",
    "id_Aisladores-S-FASE-C": "ai82",
    "id_Conectores-S-FASE-C": "ai83",
    "id_Enganche-S-FASE-C": "ai84",
    "id_Conductor-s-fase-c": "ai85",
    
    "id_Tanque Reconectador-SR-FASE-A": "al81",
    "id_Aisladores-SR-FASE-A": "al82",
    "id_Conectores-SR-FASE-A": "al83",
    "id_Enganche-SR-FASE-A": "al84",
    "id_Conductorr-sr-fase-a": "al85",
    
    "id_Tanque Reconectador-SR-FASE-B": "aq81",
    "id_Aisladores-SR-FASE-B": "aq82",
    "id_Conectores-SR-FASE-B": "aq83",
    "id_Enganche-SR-FASE-B": "aq84",
    "id_Conductorr-sr-fase-b": "aq85",
    
    "id_Tanque Reconectador-SA-FASE-A": "au81",
    "id_Aisladores-SA-FASE-A": "au82",
    "id_Conectores-SA-FASE-A": "au83",
    "id_Enganche-SA-FASE-A": "au84",
    "id_Conductor-sa-fase-a": "au85",
    
    "id_Tanque Reconectador-SA-FASE-B": "ax81",
    "id_Aisladores-SA-FASE-B": "ax82",
    "id_Conectores-SA-FASE-B": "ax83",
    "id_Enganche-SA-FASE-B": "ax84",
    "id_Conductor-sa-fase-b": "ax85",
    
    "id_Tanque Reconectador-SA-FASE-C": "ba81",
    "id_Aisladores-SA-FASE-C": "ba82",
    "id_Conectores-SA-FASE-C": "ba83",
    "id_Enganche-SA-FASE-C": "ba84",
    "id_Conductor-SA-fase-c": "ba85",
       
   
    "id_Tanque Reconectador-SR-FASE-C": "ar81",
    "id_Aisladores-SR-FASE-C": "ar82",
    "id_Conectores-SR-FASE-C": "ar83",
     "id_Enganche-SR-FASE-C": "ar84",
     "id_Conductorr-sr-fase-c": "ar85",
      
   # DPS
    "id_Estado físico equipo_SA": "bk81",
    "id_Aisladores_SA": "bk82",
    "id_Conectores_SB": "bk83",
    "id_Conductor_SA": "bk84",
    "id_Conexión_SA": "bk85",
    
    "id_Estado físico equipor_ET": "bp81",
    "id_Aisladores_ET": "bp82",
    "id_Conectores_ET": "bp83",
    "id_Conductor_ET": "bp84",
    "id_Conexión_ET": "bp85",
      
    "observaciones_10": "a87",
    
    # ============================================================================
    # PÁGINA 11: INSTALACIONES/LOCATIVAS
    # ============================================================================
    "Iluminación_Óptima_il": "n90",
    "Aseo_Óptima_il": "n91",
    "Maleza_Óptima_il": "n92",
    "Triturado_Óptima_il": "n93",
    "Encerramiento_Óptima_il": "n94",
    
    "Iluminación_Regular_il": "v90",
    "Aseo_Regular_il": "v91",
    "Maleza_Regular_il": "v92",
    "Triturado_Regular_il": "v93",
    "Encerramiento_Regular_il": "v94",
        
    "Candado_Óptima_il": "ap90",
    "Av_Óptima_il": "ap91",
    "Zvt_Óptima_il": "ax92",
    "Canal_aguas_lluvias_Óptima_il": "AP93",
    "Cámara_Vigilancia_Óptima_il": "AP94",
    
    "Candado_Regular_il": "ax90",
    "Av_Regular_il": "ax91",
    "Ztv_Regular_il": "ax92",
    "it_Canal_aguas_lluvias_Regular_RC0196_il": "AX93",
    "Cámara_Vigilancia_Regular_il": "AX94",
    
    "OBSERVACIONES_11": "ba90",
  
   
    
}


