import yfinance as yf 
import pandas as pd 
import csv
from scraper import extraer_precio

mis_activos = pd.read_csv("/Users/marcosefrainzunigahernandez/Desktop/InverTrack-Chile/data/mis_activos.csv")

columnas = mis_activos.apply("ticket")
abierto = "Close"

extraer_precio(columnas,abierto)
print(extraer_precio)