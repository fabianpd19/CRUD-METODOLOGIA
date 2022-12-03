from logicaNegocios import *
conectarMongo = PageLoader(myClient)

#ENTIDAD PROVINCIA

list = ["Azuay",
"Bolivar",
"Cañar",
"Carchi",
"Cotopaxi",
"Chimborazo",
"El Oro",
"Esmeraldas",
"Guayas",
"Imbabura",
"Loja",
"Los Rios",
"Manabi",
"Morona Santiago",
"Napo",
"Pastaza",
"Pichincha",
"Tungurahua",
"Zamora Chinchipe",
"Galapagos",
"Sucumbios",
"Orellana",
"Santa Elena",
"Santo Domingo de los Tsachilas"]



j = 1
veces = 23

for i in range(veces):  
    con = str(j)

    PROV_COD = "0"+con
    PROV_DESC = list[i]
    PROV_TAMA = ""
    PROV_HAB = ""
    PROV_HOMBRES = ""
    PROV_MUJERES = ""
    PROV_PREFECTO = ""
    PROV_FECHA = ""

    entidadProvincia = {
        'PROV_COD': PROV_COD,
        'PROV_DESC': PROV_DESC,
        'PROV_TAMA': PROV_TAMA,
        'PROV_HAB': PROV_HAB,
        'PROV_HOMBRES': PROV_HOMBRES,
        'PROV_MUJERES':PROV_MUJERES,
        'PROV_PREFECTO':PROV_PREFECTO,
        'PROV_FECHA': PROV_FECHA }

    updateDic=conectarMongo.entidadProvincia.insert_one(entidadProvincia)
    j=int(j)
    j= j+1

#####################################################################

#ENTIDAD CANTON
PROV_COD = ""
CANT_COD = ""
PARR_COD = ""
PARR_DESC = ""
PARR_URB_RUL = ""
PARR_TAM = ""
PARR_HAB = ""
PARR_HOMBRES = ""
PARR_MUJERES = ""
PARR_PRESIDENTE = ""
PARR_FECHA = ""

entidadCanton = {
    "PROV_COD": PROV_COD,
    "CANT_COD": CANT_COD,
    "PARR_COD": PARR_COD,
    "PARR_DESC": PARR_DESC,
    "PARR_URB_RUL": PARR_URB_RUL,
    "PARR_TAM": PARR_TAM,
    "PARR_HAB": PARR_HAB,
    "PARR_HOMBRES": PARR_HOMBRES,
    "PARR_MUJERES": PARR_MUJERES,
    "PARR_PRESIDENTE": PARR_PRESIDENTE,
    "PARR_FECHA": PARR_FECHA }

############################################################################

#ENTIDAD PARROQUIA

PROV_COD = ""
CANT_COD = ""
PARR_COD = ""
PARR_DESC = ""
PARR_URB_RUL = ""
PARR_TAM = ""
PARR_HAB = ""
PARR_HOMBRES = ""
PARR_MUJERES = ""
PARR_PRESIDENTE = "" 
PARR_FECHA = ""

entidadParroquia = {
    "PROV_COD": PROV_COD,
    "CANT_COD": CANT_COD,
    "PARR_COD": PARR_COD,
    "PARR_DESC": PARR_DESC,
    "PARR_URB_RUL": PARR_URB_RUL,
    "PARR_HAB": PARR_HAB,
    "PARR_HAB": PARR_HAB,
    "PARR_MUJERES": PARR_MUJERES,
    "PARR_MUJERES": PARR_MUJERES,
    "PARR_PRESIDENTE": PARR_PRESIDENTE,
    "PARR_FECHA": PARR_FECHA 
    }


########################################################    
PROV_COD = ""
CANT_COD = ""
PARR_COD = ""
COLE_COD = ""
COLE_DESC = ""
COLE_DIR = ""
COLE_TEL = ""
COLE_RECTOR = ""
COLE_SECRE = ""
COLE_INTERNET = ""

entidadParroquia = {
    "PROV_COD": PROV_COD, 
    "CANT_COD": CANT_COD, 
    "PARR_COD": PARR_COD,
    "COLE_COD": COLE_COD,
    "COLE_DESC": COLE_DESC,
    "COLE_DIR": COLE_DIR,
    "COLE_TEL": COLE_TEL,
    "COLE_RECTOR": COLE_RECTOR,
    "COLE_SECRE": COLE_SECRE,
    "COLE_INTERNET": COLE_INTERNET
}