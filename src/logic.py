import yfinance as yf 
import pandas as pd 
import requests 




status = requests.get("https://api.github.com")
print(status)

apple = yf.Ticker("SPOT")

nombre = "Apple Inc."
info_completa = apple.info
nombre_compañia = apple.info["longName"]

print(nombre_compañia)