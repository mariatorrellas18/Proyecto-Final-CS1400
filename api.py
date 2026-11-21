# Proyecto Final CS1400 - Calculadora de Distancias
# Nombre: Gabriela Torrellas y Grecia Lopez
# Fecha: 11/10/2026

import requests


# Funcion para obtener las coordenadas de una ciudad
def obtener_coordenadas(nombre_ciudad):
    """
    Consulta la API Open-Meteo para obtener
    el nombre, pais, latitud y longitud de una ciudad.
    Devuelve los datos en un diccionario.
    """

    # Direccion de la API
    url = "https://geocoding-api.open-meteo.com/v1/search"

    # Parametros para buscar la ciudad
    parametros = {
        "name": nombre_ciudad,
        "count": 1,
        "language": "es",
        "format": "json"
    }

    try:
        # Hacer la solicitud a la API
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        # Verificar si existe algun error HTTP
        respuesta.raise_for_status()

        # Convertir la respuesta a JSON
        datos = respuesta.json()

        # Verificar si la ciudad existe
        if "results" not in datos or not datos["results"]:
            return None

        # Obtener el primer resultado
        lugar = datos["results"][0]

        # Guardar la informacion de la ciudad
        info_lugar = {
            "nombre": lugar["name"],
            "pais": lugar["country"],
            "lat": lugar["latitude"],
            "lon": lugar["longitude"]
        }

        # Devolver los datos al programa principal
        return info_lugar

    # Error si la API tarda demasiado
    except requests.exceptions.Timeout as error:
        raise ConnectionError(
            "La API tardó demasiado en responder."
        ) from error

    # Error de internet o del servidor
    except requests.exceptions.RequestException as error:
        raise ConnectionError(
            "No se pudo conectar con la API. Revisa tu internet."
        ) from error

    # Error si la API devuelve datos inesperados
    except (ValueError, KeyError, TypeError, IndexError) as error:
        raise ValueError(
            "La API devolvió información inesperada."
        ) from error
