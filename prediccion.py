"""
BITACORA DEL MODELO DE MACHINE LEARNING

Proyecto: Proyeccion de Ventas Mensuales

Autor: Dariel A. Pena

Descripcion:
Script para analizar ventas historicas y generar una proyeccion
utilizando un modelo de Machine Learning basado en Regresion Lineal.
"""


# Importo las librerias necesarias para analisis, graficos y modelo lineal
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Leo el archivo de Excel y cargo la hoja Ventas en un DataFrame
df = pd.read_excel("data_venta.xlsx", sheet_name="Ventas")

# Convierto la columna Fecha a formato datetime para poder trabajar con ella
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Calculo la venta total multiplicando cantidad por precio unitario
df["Venta_Total"] = df["Cantidad"] * df["Precio_Unitario"]

# Extraigo el mes de la fecha para agrupar las ventas
df["Mes"] = df["Fecha"].dt.month

# Agrupo las ventas por mes y sumo el total vendido en cada uno
ventas_mes = df.groupby("Mes")["Venta_Total"].sum().reset_index()

# Defino la variable independiente (mes)
x = ventas_mes[["Mes"]]

# Defino la variable dependiente (ventas totales)
y = ventas_mes["Venta_Total"]

# Creo el modelo de regresion lineal
modelo = LinearRegression()

# Entreno el modelo con los datos historicos
modelo.fit(x, y)

# Defino los meses futuros para hacer la proyeccion
meses_futuros = pd.DataFrame({"Mes": [5, 6, 7, 8, 9, 10, 11, 12]})

# Genero las predicciones de ventas para los meses futuros
predicciones_futuras = modelo.predict(meses_futuros)

# Configuro el tamano del grafico
plt.figure(figsize=(8,6))

# Grafico las ventas reales por mes
plt.plot(
    ventas_mes["Mes"],
    y,
    marker="o",
    linewidth=3,
    label="Ventas Reales"
)

# Grafico la proyeccion futura de ventas
plt.plot(
    meses_futuros["Mes"],
    predicciones_futuras,
    color="green",
    linestyle="--",
    marker="o",
    linewidth=3,
    label="Proyeccion Futura"
)

# Agrego titulo y etiquetas a los ejes
plt.title("PROYECCION DE VENTAS RESTO DEL ANO")
plt.xlabel("Mes")
plt.ylabel("Ventas Totales")

# Muestro la leyenda del grafico
plt.legend()

# Agrego una cuadricula para mejor visualizacion
plt.grid(True, linestyle=":", alpha=0.6)

# Guardo el grafico como imagen en el proyecto
plt.savefig("proyeccion_ventas.png")

# Muestro el grafico en pantalla
plt.show()
