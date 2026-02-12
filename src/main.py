from scraper import extraer_precio
import yfinance as yf 

def opciones(ticket, eleccion):
   
    tipo_columna = ""
    if eleccion == 1:
        tipo_columna = "Open"
    elif eleccion == 2:
        tipo_columna = "Close"
    
   
    if tipo_columna != "":
        precio_recuperado = extraer_precio(ticket, tipo_columna)
        
        if precio_recuperado != None:
            
            informacion = yf.Ticker(ticket)
            nombre_completo = informacion.info["longName"]
            
            print(f"Empresa: {nombre_completo}")
            print(f"El precio {tipo_columna} es: {precio_recuperado:,.2f}")
        else:
            print("No se encontro el precio. Revisa el ticker.")
    else:
        print("Opcion no valida.")


nombre_empresa = input("Ingresa el ticket de la empresa: ")
opcion_usuario = int(input("Ingrese 1 para Apertura o 2 para Cierre: "))

opciones(nombre_empresa, opcion_usuario)