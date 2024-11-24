"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def ordenador(db: pd.DataFrame, col1: str, col2: str, caracter: str) -> pd.DataFrame:
    """
    Recibe un marco de datos y dos columnas. Retorna una tabla, donde
    la primera columna es cada nivel único de col1 en orden
    alfanumérico, y la segunda columna se refiere a cada uno de los
    valores col2 ordenados en orden alfanumérico, separados por
    algún caracter de interés
    """
    db = db[[col1, col2]]
    db_ord = db.sort_values(by = [col1, col2])
    db_ord.set_index(col1, inplace=True)

    retorno = {}

    for index, row in db_ord.iterrows():
        if index in retorno:
            retorno[index] += str(row[col2]) + ':' 
        else:
            retorno[index] = str(row[col2]) + ':'
    
    retorno = {key: value[:-1] for key, value in retorno.items()}

    retorno = pd.DataFrame(list(retorno.items()), columns=[col1, col2])

    retorno.set_index(col1, inplace=True)
 
    return retorno
    



def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    direccion = './files/input/tbl0.tsv'
    db0 = pd.read_csv(direccion, sep='\t')

    dbx = ordenador(db0, col1='c1', col2='c2', caracter=':')

    return dbx

#print(pregunta_10())
