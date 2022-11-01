import requests
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def datos_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            j = response.json()
            df = pd.DataFrame(j)
            df = pd.concat([df.drop(['items'], axis=1), df['items'].apply(pd.Series)], axis=1)
            return df
        
        elif response.status_code == 400:
            print("Los datos que se han enviado a la api son incorrectos. Comprueba los valores introducidos.")
        
        else: 
            print(f"Hay un error de tipo {response.status_code} en tu solicitud.")
                
    except Exception as e:
        print(e)

def info_eventos(año, mes, idioma="es"):
    idioma = idioma.lower()
    df = datos_api('http://api.euskadi.eus/culture/events/v1.0/events/byMonth/{año}/{mes}'.format(año=año, mes=mes))
    
    try:
        if idioma in ['euskera', 'eu', 'eus']:
            if 'priceEu' in df.columns:
                df = df[["typeEu", "nameEu", "municipalityEu", "establishmentEu", "openingHoursEu", "priceEu", "urlEventEu"]]
                df.columns = ["Mota", "Izena", "Udalerria", "Gunea", "Irekitze ordua", "Prezioa", "URL"]
                
            else:
                df = df[["typeEu", "nameEu", "municipalityEu", "establishmentEu", "openingHoursEu", "urlEventEu"]]
                df.columns = ["Mota", "Izena", "Udalerria", "Gunea", "Irekitze ordua", "URL"]
                
            return df
        
        elif idioma in ['español', 'es', 'esp', 'castellano']:
            if 'priceEu' in df.columns:
                df = df[["typeEs", "nameEs", "municipalityEs", "establishmentEs", "priceEs",  "openingHoursEs", "urlEventEs"]]
                df.columns = ["Tipo", "Nombre", "Municipio", "Establecimiento", "Precio", "Horario de apertura", "URL"]
                
            else:
                df = df[["typeEs", "nameEs", "municipalityEs", "establishmentEs", "openingHoursEs", "urlEventEs"]]
                df.columns = ["Tipo", "Nombre", "Municipio", "Establecimiento", "Horario de apertura", "URL"]
                
            return df
        
        else:
            print("El idioma no está disponible. Prueba 'euskera' o 'español'")
        
    except Exception as e:
        print("No hay datos para esas fechas, prueba a introducir una fecha a partir de 2018.")

def datos_año(año, grafico=True):
    try:
        df = datos_api('http://api.euskadi.eus/culture/events/v1.0/events/byYear/{año}'.format(año=año))
        df = pd.DataFrame(df.groupby(['typeEs', "municipalityEs"]).count()["id"]).reset_index()
        df.columns = ["Tipo/Mota", "Municipio/Udalerria", "Recuento/Zenbaketa"]
        if grafico:
            fig, axs = plt.subplots(ncols=2, figsize=(12,7))
            fig.tight_layout(pad=9)
            sns.barplot(data=df, x='Recuento/Zenbaketa', y='Municipio/Udalerria', color="slateblue", ax=axs[0]).set(title="{año}".format(año=año))
            sns.barplot(data=df, x='Recuento/Zenbaketa', y='Tipo/Mota', color="slateblue", ax=axs[1]).set(title="{año}".format(año=año))
        if not grafico:
            return df
    
    except TypeError:
        print("Introduce un número")
    
    except Exception as e:
        print("No hay datos para esas fechas, prueba a introducir una fecha a partir de 2018.")

def descargar(año, mes, idioma="es", formato="csv"):
    try:
        df = info_eventos(año, mes, idioma)
        formato = formato.lower()
        
        if formato == "csv":
            df.to_csv("datos_{año}_{mes}_{idioma}.csv".format(año=año, mes=mes, idioma=idioma), index=False)
            
        elif formato == "json":
            df.to_json(r"datos_{año}_{mes}_{idioma}.json".format(año=año, mes=mes, idioma=idioma))
        
        else:
            print("Formato no admitido. Formatos admitidos: 'csv' y 'json'")
            
    except AttributeError as error:
        print("No se ha podido descargar la tabla ya que no hay datos en esas fechas.")
        
    except Exception as e:
        print(e)