# importamos la libreria a usar
import pandas as pd

#leemos el archivo de excel
df = pd.read_excel("data_venta.xlsx")

#imprimimos los primeros encabezados de la data para saber si se cargo correctamente

print(df.head(15))

print(df.tail(2))

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.columns)

print(df["Categoria"])