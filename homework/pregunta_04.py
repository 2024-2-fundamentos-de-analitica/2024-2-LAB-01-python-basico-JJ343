"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    import csv

    direccion='files/input/data.csv'
    datos=[]
    with open(direccion, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila[0][9:11])
    conteo={}
    for mes in datos:
        if mes in conteo:
         conteo[mes]+=1
        else:
            conteo[mes]=1

    resultado = sorted(conteo.items())
    return resultado
pregunta_04()
