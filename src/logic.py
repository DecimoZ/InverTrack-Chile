import yfinance as yf 
import pandas as pd 
import csv
from scraper import extraer_precio
from datetime import datetime


mis_activos = pd.read_csv("C:/Users\Marcos/Desktop/InverTrack-Chile/data/mis_activos.csv") #* Ruta para abrir en win 
#mis_activos = pd.read_csv("/Users/marcosefrainzunigahernandez/Desktop/InverTrack-Chile/data/mis_activos.csv") #!ruta para abrir en mac

def crear_csv(archivo):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    extension = ".csv"
    nombre_archivo = f"C:/Users\Marcos/Desktop/InverTrack-Chile/data/{fecha_actual + extension}"
    nuevo_archivo = archivo.to_csv(nombre_archivo,index=False,encoding = "utf-8-sig")
    print(f"Su archivo fue guardado con el nombre de :{fecha_actual} y fue guardado en con la carpeta {nombre_archivo}")
    return nuevo_archivo

mis_activos["precio_actual"] = mis_activos["ticket"].apply(extraer_precio, args=("Open",))
print("-" * 50)

mis_activos["valor_total"] = mis_activos["cantidad"] * mis_activos["precio_actual"]
patrimonio_total = mis_activos["valor_total"].sum()



crear_csv(mis_activos)

 