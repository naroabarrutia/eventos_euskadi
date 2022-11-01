# Implementación y publicación de librería en PyPi
### Obtención de datos de eventos mediante api

La librería se ha desarrollado en base a los datos de eventos facilitados mediante la api de Open Data Euskadi. Se han creado diversas funciones con el fin de facilitar a los usuarios la interpretación de los datos. Las variables con las que se ha trabajado son las siguientes: 

-	Tipo de evento
-	Nombre de evento
-	Municipio
-	Establecimiento
-	Horario
-	Precio
-	Url

## Funciones 
Se han creado diversas funciones con el fin de facilitar a los usuarios la interpretación de los datos. 

| Función | Descripción | Inputs |
| ------ | ------ | ------ |
| datos_api | Utilizada por el resto de las funciones para descargar los datos deseados de la nube | Url de la api |
| info_eventos | Obtiene los datos sobre los eventos de Euskadi en un mes determinado | Mes, año e idioma (euskera o castellano)  |
| datos_año | Muestra dos gráficos de barras | Un año y un valor booleano (verdadero o falso)|
| descargar | Descarga los datos | Mes, año y un formato (csv o json) |

## Estructura de archivos 
```sh
ejemplos 
    datos_año.JPG
```

```sh
eventos_euskadi
    eventos_euskadi.py
    __init__.py
```

```sh
LICENSE.txt
```

```sh
README.md
```

```sh
setup.cfg
```

```sh
setup.py
```
## Dependencias 
- [Pandas] - Proporciona herramientas que permiten trabajar datos en diferentes formatos.
- [Matplotlib] - Creación de gráficos en dos dimensiones.
- [Request] - Obtener respuestas que se realizan en el protocolo HTTP de una plataforma web que se haya establecido con anterioridad con una API.
- [Seaborn] - Visualizaciones de datos.

## Uso
```python
import eventos_euskadi as ev

# Se obtiene información sobre eventos en un mes
ev.info_eventos(2021, 1, 'eus')

# Se descargan datos de eventos en un mes
ev.descargar(2021, 5, 'es', 'csv')

# Se muestran dos gráficos con información sobre eventos en un año 
ev.datos_año(2021, True)
```

![Alt text](https://github.com/naroabarrutia/eventos_euskadi/blob/main/ejemplos/datos_año.JPG?raw=true)

## Licencia
[MIT]

## Autores 
>Mikel Madariaga & Naroa Barrutia 

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen)

[Pandas]: <https://pandas.pydata.org/>
[Matplotlib]: <https://matplotlib.org/>
[Request]: <https://pypi.org/project/requests/>
[Seaborn]: <https://seaborn.pydata.org/>
[MIT]: <https://choosealicense.com/licenses/mit/>