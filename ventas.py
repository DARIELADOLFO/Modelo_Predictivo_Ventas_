# importamos la libreria a usar
import pandas as pd
import matplotlib.pyplot as plt

#leemos el archivo de excel
df = pd.read_excel("data_venta.xlsx")

#para tener una informacion completa de la data
print(df.info())

#contamos los valores de la categoria
ventas_categorias = df["Categoria"].value_counts()

#seleccionamos y creamos nuestro grafico
ventas_categorias.plot(
    kind="bar", 
    color="black"
    )

#mostramos el grafico
plt.show()

#seleccionamos el 2do grafico
df["Ciudad"].value_counts().plot(
    kind="barh", 
    color="orange"
    )
#mostramos el titulo
plt.title(
    "Ventas Ciudad"
    )

#mostramos el grafico
plt.show()