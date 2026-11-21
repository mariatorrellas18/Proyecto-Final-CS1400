# Pseudocódigo V2 – Calculadora de Distancias

Para el Paso 7 de nuestro proyecto final CS1400, reorganizamos nuestra calculadora utilizando Programación Orientada a Objetos (POO).

Creamos una clase llamada `Ciudad` en el archivo `ciudad.py`, que contiene cuatro atributos: nombre, país, latitud y longitud. Utilizamos el constructor `__init__()` para guardar estos datos y el método `__str__()` para mostrar la información de cada ciudad.

También agregamos el método `distancia_a()`, que permite calcular la distancia entre dos objetos Ciudad utilizando la función `calcular_distancia()` del archivo `utils.py`, donde aplicamos la fórmula de Haversine.

En `main.py`, el usuario ingresa las ciudades de origen y destino. El programa consulta sus coordenadas mediante `api.py` y crea dos objetos de la clase `Ciudad`. Después calcula la distancia utilizando `origen.distancia_a(destino)`, realiza la conversión a millas y estima los tiempos de viaje en avión y automóvil.

Finalmente, muestra un resumen del viaje y regresa al menú principal, permitiendo realizar otro cálculo o salir del programa.