# importamos la libreria a usar
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# leemos el archivo de excel
df = pd.read_excel("data_venta.xlsx", sheet_name="Ventas")

# CORRECCIÓN 1: Signo de igual para asignar
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Venta_Total"] = df["Cantidad"] * df["Precio_Unitario"]
df["Mes"] = df["Fecha"].dt.month

# CORRECCIÓN 2: Paréntesis al final de reset_index()
ventas_mes = df.groupby("Mes")["Venta_Total"].sum().reset_index()

x = ventas_mes[["Mes"]]
# CORRECCIÓN 3: "T" mayúscula y un solo corchete
y = ventas_mes["Venta_Total"]

modelo = LinearRegression()
modelo.fit(x, y)

# prediccion
meses_futuros = pd.DataFrame({"Mes": [5, 6, 7, 8, 9, 10, 11, 12]})
predicciones_futuras = modelo.predict(meses_futuros)

# visualizar resultado
plt.figure(figsize=(8,6))

# linea de ventas
plt.plot(ventas_mes["Mes"], y, marker="o", linewidth=3, label="Ventas Reales")

# linea prediccion
plt.plot(meses_futuros["Mes"], predicciones_futuras, color="green", linestyle="--", marker="o", linewidth=3, label="Proyeccion Futura")

# detalles
plt.title("PROYECCION DE VENTAS RESTO DEL ANO")
plt.xlabel("Mes")
plt.ylabel("Ventas Totales")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)

#Aqui para descargar la imagen :
plt.savefig("proyeccion_venddtas.png")


# mostrar grafico
plt.show()

