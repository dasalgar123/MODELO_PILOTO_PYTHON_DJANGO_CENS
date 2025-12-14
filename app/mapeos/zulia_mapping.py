# ============================================================================
# MAPEO PARA FORMULARIO S_XX_ZULIA
# ============================================================================
import os

# Mapeo: Encabezado + PÁGINA 2 - FORMULARIO S_XX_ZULIA
zulia_mapping = {

    # Encabezado PÁGINA 2-->
    "fecha": "AP5",
    "ejecuto": "K6",
    "numero_ot": "K5",
    # FILA 2 PÁGINA 2-->
    # FILA 2 PÁGINA 2-->
    # FILA 3 PÁGINA 2-->
    # FILA 4 PÁGINA 2-->
    "id_EFT_fa_rc_t2" : "N15",

    "id_EFT_fa_tc_t2" : "AF15",
    "id_EFT_fb_tc_t2" : "AI15",
    "id_EFT_fc_tc_t2" : "AL15",

    "id_EFT_fa_tt_t2" : "BB15",
    "id_EFT_fb_tt_t2" : "BE15",
    "id_EFT_fc_tt_t2" : "BH15",

    # FILA 5 PÁGINA 2-->
    "id_EFG_fa_rc_t2": "N16",
    
    "id_Ce_fa_tc_t2": "AF16",
    "id_Ce_fb_tc_t2" : "AI16",
    "id_Ce_fc_tc_t2" : "AL16",
    
    "id_Ce_fa_tt_t2": "BB16",
    "id_Ce_fb_tt_t2": "BE16",
    "id_Ce_fc_tt_t2": "BH16",
    
    # FILA 6 PÁGINA 2-->
    "id_B_rc_t2" : "N17",
    "id_Cs_fa_tc_t2"  : "AF17",
    "id_Cs_fb_tc_t2"  : "AI17",
    "id_Cs_fc_tc_t2"  : "AL17",
    
    "id_Cs_fa_tt_t2": "BB17",
    "id_Cs_fb_tt_t2": "BE17",
    "id_Cs_fc_tt_t2": "BH17",
    
    # FILA 7 PÁGINA 2-->
    "id_D_rc_t2": "N18",
    
    "id_Cpt_fa_tc_t2": "AF18",
    "id_Cpt_fb_tc_t2": "AI18",
    "id_Cpt_fc_tc_t2": "AL18",
    
    "id_Cpt_fa_tt_t2": "BB18",
    "id_Cpt_fb_tt_t2": "BE18",
    "id_Cpt_fc_tt_t2": "BH18",
    
    # FILA 8 PÁGINA 2-->
    
    "id_Ag_rc_t2": "N19",
    
    "id_Cpt_fa_tc_t2": "AF19",
    "id_Cpt_fb_tc_t2": "AI19",
    "id_Cpt_fc_tc_t2": "AL19",
    
    "id_Cpt_fa_tt_t2": "BB19",
    "id_Cpt_fb_tt_t2": "BE19",
    "id_Cpt_fc_tt_t2": "BH19",
    
    # FILA 9 PÁGINA 2-->
    "id_ORrc_t2": "N20",
    # FILA 10 PÁGINA 2-->
    "observaciones_2": "S21",
    # FILA 11 PÁGINA 2-->
    "id_PAC_rc_t2": "N21",
    # FILA 12 PÁGINA 2-->
    "id_PDC_rc_t2": "N22",
    # FILA 13 PÁGINA 2-->
    "id_Nm_rc_t2": "N23",
    
    # FILA Encabezado PÁGINA 3-->
    # FILA 1 PÁGINA 3-->
    # FILA 2 PÁGINA 3-->
    
    "it_Aceite_t3": "O27",
    "it_At_t3": "U27",
    "It_Bt_t3": "Z27",
    
    "it_T_t3": "AE27",
    "it_C_t3": "AI27",
    
    "it_p_t3": "AO27",
    "it_Nm_t3": "AT27",
    
    "it_80_Cuba": "AZ28",
    "it_80_OLTC": "BI28",
    
    # FILA 3 PÁGINA 3-->
    "it_25_Cuba": "AZ30",
    "it_25_OLTC": "BI30",
    # FILA 4 PÁGINA 3-->
    
    "it_FRA": "G31",
    "it_FRB": "K31",
    
    "it_Observaciones_3": "O30",
    
    "it_20_Cuba": "AZ32",
    "it_20_OLTC": "BI32",
    
    # FILA 5 PÁGINA 3-->
    
    "it_FSA": "G32",
    "it_FSB": "K32",
    # FILA 6 PÁGINA 3-->
    
    "it_FTA": "G33",
    "it_FTB": "K33",
    
    # FILA Encabezado PÁGINA 4-->
    # FILA 1 PÁGINA 4-->
    # FILA 2 PÁGINA 4-->
    # FILA 3 PÁGINA 4-->
    
    "it_Ce_fr_tc_t4": "O41",
    "it_Ce_fs_tc_t4": "R41",
    "it_Ce_ft_tc_t4": "U41",
    
    "Ce_fr_tt_t4": "AK41",
    "Ce_fs_tt_t4": "AN41",
    "Ce_ft_tt_t4": "AQ41",
    "it_OBSERVACIONES_4": "AT38",
    # FILA 4 PÁGINA 4-->
    "it_Cs_fr_tc_t4":"O42",
    "it_Cs_fs_tc_t4":"R42",
    "it_Cs_ft_tc_t4":"U42",
    
    "it_Cs_fr_tt_t4": "AK42",
    "it_Cs_fs_tt_t4": "AN42",
    "it_Cs_ft_tt_t4": "AQ42",
    # FILA 5 PÁGINA 4-->
    "it_Cs_fr_tc_t4": "O43",
    "it_Cs_fs_tc_t4": "R43",
    "it_Cs_ft_tc_t4": "U43",
    
    "it_Cs_fr_tt_t4": "AK43",
    "it_Cs_fs_tt_t4": "AN43",
    "it_Cs_ft_tt_t4": "AQ43",
    # FILA 6 PÁGINA 4-->
    "it_Cpt_fr_t4": "O44",
    "it_Cpt_fs_t4": "R44",
    "it_Cpt_ft_t4": "U44",
    
    "it_Cpt_fr_tt_t4": "AK44",
    "it_Cpt_fs_tt_t4": "AN44",
    "it_Cpt_ft_tt_t4": "AQ44",
     # FILA 7 PÁGINA 4-->
    "it_Cpt_fr_t4": "O45",
    "it_Cpt_fs_t4": "R45",
    "it_Cpt_ft_t4": "U45",
    
    "it_Cpt_fa_t4": "AK45",
    "it_Cpt_fb_t4": "AN45",
    "it_Cpt_fc_t4": "AQ45",
    
    # FILA Encabezado PÁGINA 5-->
    # FILA 1 PÁGINA 5-->
    # FILA 2 PÁGINA 5-->
    "it_EFT_rca": "P49",
    "it_EFT_rcb": "AK49",
    "it_EFT_rcz": "BF49",
    # FILA 3 PÁGINA 5-->
    "it_EFG_rca": "P50",
    "it_EFG_rcb": "AK50",
    "it_EFG_rcz": "BF50",
    # FILA 4 PÁGINA 5-->
    "it_B_rca": "P51",
    "it_B_rcb": "AK51",
    "it_B_rcz": "BF51",
    # FILA 5 PÁGINA 5-->
    "it_D_rca": "P52",
    "it_D_rcb": "AK52",
    "it_D_rcz": "BF52",
    # FILA 6 PÁGINA 5-->
    "it_Ag_rca": "P53",
    "it_Ag_rcb": "AK53",
    "it_Ag_rcz": "BF53",
    # FILA 7 PÁGINA 5-->
    "it_OR_rca": "P54",
    "it_OR_rcb": "AK54",
    "it_OR_rcz": "BF54",
    # FILA 8 PÁGINA 5-->
    "it_PAC_rca": "P55",
    "it_PAC_rcb": "AK55",
    "it_PAC_rcz": "BF55",
    # FILA 9 PÁGINA 5-->
    "it_PDC_rca": "P56",
    "it_PDC_rcb": "AK56",
    "it_PDC_rcz": "BF56",
    # FILA 10 PÁGINA 5-->
    "it_Nm_rca": "P57",
    "it_Nm_rcb": "AK57",
    "it_Nm_rcz": "BF57",
    
    # FILA Encabezado PÁGINA 6-->
    # FILA 1 PÁGINA 6-->
    # FILA 2 PÁGINA 6-->
    "it_io_mc": "V67",
    "it_Ir_mc": "AE67",
    "it_ao_gp": "BA67",
    "it_ar_gp": "BI67",
    # FILA 3 PÁGINA 6-->
    "it_AÓ_mc": "V68",
    "it_AR_mc": "AE68",
    "it_IÓ_gp": "BA68",
    "it_IR_gp": "BI68",
    # FILA 4 PÁGINA 6-->
    "it_EeÓ_mc": "V69",
    "it_Eer_mc": "AE69",
    "LoÓ_gp": "BA69",
    "LoR_gp": "BI69",
    # FILA 5 PÁGINA 6-->
    "it_UÓ_mc": "V70",
    "it_UR_mc": "AE70",
    "it_CÓ_gp": "BA70",
    "it_CR_gp": "BI70",
    # FILA 6 PÁGINA 6-->
    "it_Bbt_Ómc": "V71",
    "it_Bbt_R_mc": "AE71",
    "it_EG_Ó_gp": "BA71",
    "it_EG_R_gp": "BI71",
    # FILA 7 PÁGINA 6-->
    "OBSERVACIONES_6a": "B73",
    "OBSERVACIONES_6b": "AG73",
    
    # FILA Encabezado PÁGINA 7-->
    # FILA 1 PÁGINA 7-->
    # FILA 2 PÁGINA 7-->
    "it_I_IG": "L78",
    "it_Aa_IG": "AA78",
    "OBSERVACIONES_7": "AG78",
    # FILA 3 PÁGINA 7-->
    "it_A_IG": "L79",
    "it_Eb_IG": "AA79",
    # FILA 4 PÁGINA 7-->
    "it_Mz_IG": "L80",
    "it_M_IG": "AA80",
    # FILA 5 PÁGINA 7-->
    "it_E_IG": "L81",
    "it_TSA_IG": "AA81",
    # FILA 6 PÁGINA 7-->
    "it_L_IG": "L82",
    "it_VSA_IG": "AA82",
    # FILA 7 PÁGINA 7-->
    "it_TC_IG": "L83",
    "it_CSA_IG": "AA83",
    # FILA 8 PÁGINA 7-->
    "it_E_IG": "L84",
  
    # FILA Encabezado PÁGINA 8-->
    # FILA 1 PÁGINA 8-->
    # FILA 2 PÁGINA 8-->
    "it_EI_ig": "L89",
    "it_PS_ig": "AA89",
    "OBSERVACIONES_8": "AG78",
    # FILA 3 PÁGINA 8-->
    "it_BDC_ig": "L90",
    "it_Ee_ig": "AA90",
    # FILA 4 PÁGINA 8-->
    "it_BAC_ig": "L91",
    "it_Br_ig": "AA91",
    # FILA 5 PÁGINA 8-->
    "it_Led's_de_Operación_ig": "L92",
    "it_Estado_gabinete_ig": "AA92",
    # FILA 6 PÁGINA 8-->
    "it_LG_ig": "L93",
    "it_Vb_ig": "AA93",
    # FILA 7 PÁGINA 8-->
    "it_ST_ig": "L94",
    "it_VP_ig": "AA94",
      
    
    
    # FIRMA DIGITAL (se inserta como imagen, no como texto)
    # El campo "firma_digital" del formulario se inserta como imagen en la celda K96
    # Ver: ZULIA_CONFIG['firma_celda'] = 'K96'


# ============================================================================
# CONFIGURACIÓN DEL FORMULARIO S_XX_ZULIA
# ============================================================================
ZULIA_CONFIG = {
    'mapping': zulia_mapping,
    'template': 'subestacion/S_XX_ZULIA/s_xx_zulia.html',
    'excel_template': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'plantillas_excel', 'PLT_201_MST_022_EL ZULIA.xlsx'),
    'excel_sheet': 'PLT_201_MST_022',
    'file_prefix': 'S_XX_ZULIA',
    'firma_celda': 'K96',
}

