"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

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
        key = row[0]  
    
    
        for i in range(3, len(row)):
            if ':' in row[i]:  
            
                for element in row[i:]:
                 if ':' in element:
                    value = int(element.split(':')[1]) 
                    sum_dict[key] += value  
                break  


    sorted_sum_dict = dict(sorted(sum_dict.items()))


    return sorted_sum_dict

pregunta_12()