"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    import csv
    from collections import defaultdict



    direccion='files/input/data.csv'
    data=[]
    with open(direccion, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                fila_limpia=[ item for sublist in [x.replace(",","\t").split("\t")for x in fila ]for item in sublist]
                data.append(fila_limpia)
    assoc_dict = defaultdict(set)  # Usamos set para evitar letras repetidas


    for row in data:
        letter = row[0]  
        value = int(row[1])  
    

        assoc_dict[value].add(letter)


    result = sorted((key, sorted(list(value))) for key, value in assoc_dict.items())


    return result
pregunta_08()