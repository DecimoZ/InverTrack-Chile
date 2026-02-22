import yfinance as yf 
import pandas as pd 
import csv
from scraper import extraer_precio


mis_activos = pd.read_csv("C:/Users\Marcos/Desktop/InverTrack-Chile/data/mis_activos.csv") #* Ruta para abrir en win 
#mis_activos = pd.read_csv("/Users/marcosefrainzunigahernandez/Desktop/InverTrack-Chile/data/mis_activos.csv") #!ruta para abrir en mac

def crear_csv(archivo):
    nombre = input("Ingrese el nombre para el archivo:")
    nuevo_archivo = archivo.to_csv(f"C:/Users\Marcos/Desktop/InverTrack-Chile/data/{nombre +".csv"}",index=False)
    return nuevo_archivo

mis_activos["precio_actual"] = mis_activos["ticket"].apply(extraer_precio, args=("Open",))
print("-" * 50)

mis_activos["valor_total"] = mis_activos["cantidad"] * mis_activos["precio_actual"]
patrimonio_total = mis_activos["valor_total"].sum()



crear_csv(mis_activos)

 