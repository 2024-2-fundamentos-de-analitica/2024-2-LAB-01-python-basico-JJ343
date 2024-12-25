"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


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

   
    sum_dict = defaultdict(int)


    for row in data:
        value = int(row[1])  

    
        for i in range(3, len(row)):
            if ':' in row[i]:
             break
            letter = row[i]  
            sum_dict[letter] += value  


    sorted_sum_dict = dict(sorted(sum_dict.items()))

    return sorted_sum_dict
pregunta_11()