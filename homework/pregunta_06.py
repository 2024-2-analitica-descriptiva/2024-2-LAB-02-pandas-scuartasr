"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    import pandas as pd

    direccion = './files/input/tbl1.tsv'
    db1 = pd.read_csv(direccion, sep = '\t')

    c4 = db1.c4.unique()

    c4 = [x.upper() for x in c4]

    return sorted(c4)


#print(pregunta_06())
