"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

from homework import pregunta_11
import pandas as pd

def unificador(
          db: pd.DataFrame,
          col1: str, col2: str, col3,
          sep: str
     ) -> pd.DataFrame:
     """
     Esta función crea una columna llamada col3 que es el resultado
     de concatenar las columnas col1 y col2. Además, están separadas
     por el string sep
     """

     db[col3] = db[col1].astype(str) + sep + db[col2].astype(str)

     return db


def pregunta_12():
     """
     Construya una tabla que contenga `c0` y una lista separada por ','
     de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
     tabla `tbl2.tsv`.

     Rta/
          c0                                   c5
     0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
     1     1              aaa:3,ccc:2,ddd:0,hhh:9
     2     2              ccc:6,ddd:2,ggg:5,jjj:1
     ...
     37   37                    eee:0,fff:2,hhh:6
     38   38                    eee:0,fff:9,iii:2
     39   39                    ggg:3,hhh:8,jjj:5
     """

     direccion = './files/input/tbl2.tsv'
     db2 = pd.read_csv(direccion, sep='\t')

     db2 = unificador(db2, col1='c5a', col2='c5b', col3='c5', sep=':')

     db2 = db2[['c0', 'c5']].sort_values(by=['c0', 'c5'])

     dbx = pregunta_11.ordenador(
          db=db2, col1='c0', col2='c5', sep=',', tipo='df'
     )

     return dbx

#print(pregunta_12())



