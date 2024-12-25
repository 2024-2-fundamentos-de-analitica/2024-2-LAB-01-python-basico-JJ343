"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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

    value_dict = defaultdict(lambda: [float('inf'), float('-inf')])  # [min_value, max_value]
    for row in data:
        for entry in row:  
            if ':' in entry:  
                key, value = entry.split(':')
                value = int(value)  

            
                value_dict[key][0] = min(value_dict[key][0], value)
                value_dict[key][1] = max(value_dict[key][1], value)


    result = [(key, value[0], value[1]) for key, value in value_dict.items()]


    sorted_results =sorted(result, key=lambda x: x[0])
    return sorted_results           
                
pregunta_06()