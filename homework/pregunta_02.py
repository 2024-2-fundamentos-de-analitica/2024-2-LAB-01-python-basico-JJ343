"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    import csv
    from collections import Counter



    direccion='files/input/data.csv'
    string=""
    with open(direccion, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
         string+=fila[0][0]
    conteo=Counter(string)
    resultado=sorted(conteo.items())
    return resultado

pregunta_02()
