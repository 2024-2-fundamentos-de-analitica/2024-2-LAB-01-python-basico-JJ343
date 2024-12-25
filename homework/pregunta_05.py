"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

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

    valores_por_letra = defaultdict(lambda: {'max': float('-inf'), 'min': float('inf')})

    for letra, valor in datos:
        valores_por_letra[letra]['max'] = max(valores_por_letra[letra]['max'], int(valor))
        valores_por_letra[letra]['min'] = min(valores_por_letra[letra]['min'], int(valor))

    resultado = [(letra, valores['max'], valores['min']) for letra, valores in sorted(valores_por_letra.items())]

    return(resultado)
pregunta_05()
