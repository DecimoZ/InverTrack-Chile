import yfinance as yf 
import pandas as pd

def extraer_precio(empresa,tipo_data):
    nombre_empresa = yf.Ticker(empresa)
    historial = nombre_empresa.history(period = "1d")

    if historial.empty:
        print("Error en el dato, no hay nada que procesar")
        return None
    else:
        ultimo_precio = historial[tipo_data].iloc[-1]
        return ultimo_precio































#! Funcion que devuelve el precio de cierre
def Precio_de_cierre(Empresa):
    ticket = yf.Ticker(Empresa)
    cierre = ticket.history(period="1d")
    
    if cierre.empty:
        print("Error en el dato, no hay nada que procesar")
        return None
    else:
        ultimo_precio = cierre["Close"].iloc[-1]
        return ultimo_precio
    
    
def Precio_de_Apertura(Empresa):
    ticket = yf.Ticker(Empresa)
    apertura = ticket.history(period="1d")
    
    if apertura.empty:
        print("Error en el dato, no hay nada que procesar")
        return None
    else:
        precio_inicial = apertura["Open"].iloc[-1]
        return precio_inicial
    

