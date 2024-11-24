"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def reorganizar(
        db1: pd.DataFrame, db2: pd.DataFrame
) -> pd.DataFrame:
    
    if len(db1) >= len(db2):
        return db1, db2
    else:
        return db2, db1

def cruce_izq(
        db1: pd.DataFrame, db2: pd.DataFrame
) -> pd.DataFrame:
    """
    Esta función retorna el cruce entre db1 y db2, donde db1 es
    la tabla de la izquierda
    """

    # Selección de tabla de la izquierda
    db1, db2 = reorganizar(db1, db2)

    db3 = pd.merge(
        db1, db2,
        on='c0',
        how='left'
    )
    
    return db3

def sumador(
        db: pd.DataFrame, col1: str, col2: str
) -> pd.DataFrame:
    """
    Esta funciona agrupa los niveles de col1 y suma los valores de col2
    correspondientes
    """
    db = db.groupby([col1])[col2].sum()
    
    return db

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    direccion1 = './files/input/tbl0.tsv'
    db1 = pd.read_csv(direccion1, sep='\t')

    direccion2 = './files/input/tbl2.tsv'
    db2 = pd.read_csv(direccion2, sep='\t')

    db = cruce_izq(db1, db2)

    db = sumador(db, col1='c1', col2='c5b')

    return db

#print(pregunta_13())
