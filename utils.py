
# Proyecto Final CS1400 - Calculadora de Distancias
# Nombre: Gabriela Torrellas y Grecia Lopez

import math


# Funcion para calcular la distancia entre dos ciudades
def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en linea recta entre dos puntos
    utilizando la formula de Haversine.
    Devuelve la distancia en kilometros.
    """

    # Convertir las coordenadas a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Formula de Haversine
    diferencia_lat = lat2 - lat1
    diferencia_lon = lon2 - lon1

    a = (math.sin(diferencia_lat / 2) ** 2 +
         math.cos(lat1) * math.cos(lat2) *
         math.sin(diferencia_lon / 2) ** 2)

    a = max(0, min(1, a))

    c = 2 * math.asin(math.sqrt(a))

    # Radio de la Tierra en kilometros
    distancia = 6371 * c

    return round(distancia, 2)
