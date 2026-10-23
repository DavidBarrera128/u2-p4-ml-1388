import pandas as pd
import numpy as np
# David Barrera NC = 1388
n_filas = 5
n_columnas = 5
tag_columnas = tuple("ABCDE") # etiquetas para las columnas d euna tupla
print(tag_columnas)
matriz = np.random.randint(1, 10, size = (n_filas, n_columnas))
print("gnera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendido entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df = pd.DataFrame(matriz, columns= tag_columnas)
print("--- La tabla o DataFrame --- NC = 1388 ---")
print(df)
print("---- David Barrera NC = 1388 ----")