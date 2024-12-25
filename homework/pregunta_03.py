"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    import csv
    from collections import defaultdict



    direccion='files/input/data.csv'
    datos=[]
    with open(direccion, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                caja=(fila[0][0],fila[0][2])
                datos.append(caja)

    suma_letra =defaultdict(int)

    for letra, valor  in datos:
     suma_letra[letra] += int(valor)

    resultado=sorted(suma_letra.items())
    return resultado

pregunta_03()