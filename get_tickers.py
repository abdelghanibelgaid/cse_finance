def get_tickers():
    data = """[{"Titre": "AFMA","Ticker": "AFM"},{"Titre": "AFRIC INDUSTRIES SA","Ticker": "AFI"},{"Titre": "AFRIQUIA GAZ","Ticker": "GAZ"},
    {"Titre": "AGMA","Ticker": "AGM"},{"Titre": "ALLIANCES","Ticker": "ADI"},{"Titre": "ALUMINIUM DU MAROC","Ticker": "ALM"},
    {"Titre": "ARADEI CAPITAL","Ticker": "ARD"},{"Titre": "ATLANTASANAD","Ticker": "ATL"},{"Titre": "ATTIJARIWAFA BANK","Ticker": "ATW"},
    {"Titre": "AUTO HALL","Ticker": "ATH"},{"Titre": "AUTO NEJMA","Ticker": "NEJ"},{"Titre": "BALIMA","Ticker": "BAL"},
    {"Titre": "BANK OF AFRICA","Ticker": "BOA"},{"Titre": "BCP","Ticker": "BCP"},{"Titre": "BMCI","Ticker": "BCI"},
    {"Titre": "CARTIER SAADA","Ticker": "CRS"},{"Titre": "CDM","Ticker": "CDM"},{"Titre": "CENTRALE DANONE","Ticker": "CDA"},
    {"Titre": "CIH","Ticker": "CIH"},{"Titre": "CIMENTS DU MAROC","Ticker": "CMA"},{"Titre": "CTM","Ticker": "CTM"},
    {"Titre": "COLORADO","Ticker": "COL"},{"Titre": "COSUMAR","Ticker": "CSR"},{"Titre": "CTM","Ticker": "CTM"},
    {"Titre": "DARI COUSPATE","Ticker": "DRI"},{"Titre": "DELATTRE LEVIVIER MAROC","Ticker": "DLM"},{"Titre": "DELTA HOLDING","Ticker": "DHO"},
    {"Titre": "DIAC SALAF","Ticker": "DIS"},{"Titre": "DISWAY","Ticker": "DWY"},{"Titre": "DOUJA PROM ADDOHA","Ticker": "ADH"},
    {"Titre": "ENNAKL","Ticker": "NKL"},{"Titre": "EQDOM","Ticker": "EQD"},{"Titre": "FENIE BROSSETTE","Ticker": "FBR"},
    {"Titre": "HPS","Ticker": "HPS"},{"Titre": "IB MAROC.COM","Ticker": "IBC"},{"Titre": "IMMORENTE INVEST","Ticker": "IMO"},
    {"Titre": "INVOLYS","Ticker": "INV"},{"Titre": "ITISSALAT AL-MAGHRIB","Ticker": "IAM"},{"Titre": "JET CONTRACTORS","Ticker": "JET"},
    {"Titre": "LABEL VIE","Ticker": "LBV"},{"Titre": "LAFARGEHOLCIM MAR","Ticker": "LHM"},{"Titre": "LESIEUR CRISTAL","Ticker": "LES"},
    {"Titre": "LYDEC","Ticker": "LYD"},{"Titre": "M2M Group","Ticker": "M2M"},{"Titre": "MAGHREB OXYGENE","Ticker": "MOX"},
    {"Titre": "MAGHREBAIL","Ticker": "MAB"},{"Titre": "MANAGEM","Ticker": "MNG"},{"Titre": "MAROC LEASING","Ticker": "MLE"},
    {"Titre": "MED PAPER","Ticker": "MDP"},{"Titre": "MICRODATA","Ticker": "MIC"},{"Titre": "MINIERE TOUISSIT","Ticker": "CMT"},
    {"Titre": "MUTANDIS SCA","Ticker": "MUT"},{"Titre": "Oulmes","Ticker": "OUL"},{"Titre": "PROMOPHARM","Ticker": "PRO"},
    {"Titre": "REALISATIONS MECANIQUES","Ticker": "SNP"},{"Titre": "REBAB COMPANY","Ticker": "REB"},{"Titre": "RES DAR SAADA","Ticker": "RDS"},
    {"Titre": "RISMA","Ticker": "RISMA"},{"Titre": "S.M MONETIQUE","Ticker": "S2M"},{"Titre": "SAHAM ASSURANCE","Ticker": "SAH"},
    {"Titre": "SALAFIN","Ticker": "SLF"},{"Titre": "SAMIR","Ticker": "SAM"},{"Titre": "SMI","Ticker": "SMI"},{"Titre": "SNEP","Ticker": "SNA"},
    {"Titre": "SOCIETE DES BOISSONS DU MAROC","Ticker": "SBM"},{"Titre": "SODEP-Marsa Maroc","Ticker": "MSA"},{"Titre": "SONASID","Ticker": "SID"},
    {"Titre": "SOTHEMA","Ticker": "SOT"},{"Titre": "STOKVIS NORD AFRIQUE","Ticker": "SBM"},{"Titre": "STROC INDUSTRIE","Ticker": "STR"},
    {"Titre": "TAQA MOROCCO","Ticker": "TQM"},{"Titre": "TIMAR","Ticker": "TIM"},{"Titre": "TOTALENERGIES MARKETING MAROC","Ticker": "TMA" },
    {"Titre": "UNIMER","Ticker": "UMR"},{"Titre": "WAFA ASSURANCE","Ticker": "WAA"},{"Titre": "ZELLIDJA S.A","Ticker": "ZDJ"}]"""
    
    df = _pd.read_json(data)
    _pd.set_option('display.max_rows', 100)
    
    return df
