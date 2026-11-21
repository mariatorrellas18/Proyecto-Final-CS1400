"""
Bienvenida a nuestro proyecto final de CS1400, donde exploraremos y aplicaremos los conceptos aprendidos a lo largo del curso.
- Gabriela Torrellas y Grecia Lopez.
"""

# Nombre: Gabriela Torrellas y Grecia Lopez
# Fecha: 11/10/2026
# Proyecto Final CS1400 - Calculadora de Distancias

from api import obtener_coordenadas, calcular_distancia

# Velocidades promedio para estimar los tiempos de viaje
# Se utilizan valores aproximados en kilometros por hora
VELOCIDAD_AVION = 800
VELOCIDAD_AUTO = 80



# Funcion para mostrar el menu principal
def mostrar_menu():
    """Muestra la bienvenida y las opciones del menu."""
    print("\n=== Calculadora de Distancias ===")
    print("¡Bienvenida turista, comencemos nuestra aventura!")
    print("1. Calcular distancia")
    print("2. Salir")


# Funcion para pedir la ciudad de origen o destino
def pedir_ciudad(mensaje):
    """Solicita una ciudad y no permite entradas vacias."""
    while True:
        ciudad = input(mensaje).strip()

        if ciudad != "":
            return ciudad
        else:
            print("Error: No puedes dejar este campo vacio.")


# Funcion para consultar las coordenadas de una ciudad
def consultar_ciudad(mensaje):
    """
    Busca una ciudad usando la API.
    Si la ciudad no existe, regresa al menu principal.
    Si ocurre un error de conexion, muestra el error.
    """

    ciudad = pedir_ciudad(mensaje)

    try:
        datos = obtener_coordenadas(ciudad)

        if datos is None:
            print("Ciudad no encontrada.")
            return None

        return datos

    except ConnectionError as error:
        print(f"Error de conexion: {error}")
        return None

    except ValueError as error:
        print(f"Error en los datos de la API: {error}")
        return None


    while True:
        ciudad = pedir_ciudad(mensaje)

        try:
            datos = obtener_coordenadas(ciudad)

            if datos is not None:
                return datos
            else:
                print("Ciudad no encontrada. Intenta con otra ciudad.")

        except (ConnectionError, ValueError) as error:
            print(f"Error: {error}")
            return None


# Funcion para seleccionar la unidad
def pedir_unidad():
    """Permite elegir entre kilometros y millas."""
    while True:
        unidad = input("Unidad (km/millas): ").strip().lower()

        if unidad == "km":
            return "kilómetros"

        elif unidad == "millas":
            return "millas"

        else:
            print("Error: Debes escribir km o millas.")


# Funcion para convertir horas decimales a horas y minutos
def convertir_tiempo(horas):
    """
    Convierte las horas decimales al formato
    de horas y minutos.
    """

    minutos_totales = round(horas * 60)

    horas_enteras = minutos_totales // 60
    minutos = minutos_totales % 60

    return f"{horas_enteras} h {minutos} min"


# Funcion para mostrar el resumen
def mostrar_resumen(origen, destino, unidad):
    """Muestra un resumen de los datos ingresados."""
    print("\n--- Resumen ---")
    print(f"Origen:  {origen}")
    print(f"Destino: {destino}")
    print(f"Unidad:  {unidad}")
    print("Consultando datos...")


# Funcion para mostrar las coordenadas
def mostrar_coordenadas(origen, destino):
    """Muestra las coordenadas obtenidas de la API."""

    print("\n--- Coordenadas obtenidas ---")

    print(
        f"Origen: {origen['nombre']}, {origen['pais']} "
        f"-> lat {origen['lat']:.4f}, lon {origen['lon']:.4f}"
    )

    print(
        f"Destino: {destino['nombre']}, {destino['pais']} "
        f"-> lat {destino['lat']:.4f}, lon {destino['lon']:.4f}"
    )


# Funcion principal del programa
def main():
    """Ejecuta el programa hasta que el usuario elija salir."""

    while True:
        mostrar_menu()

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print()

            # Solicitar la ciudad de origen
            datos_origen = consultar_ciudad("Ciudad de origen: ")

            if datos_origen is None:
                continue

            # Solicitar la ciudad de destino
            datos_destino = consultar_ciudad("Ciudad de destino: ")

            if datos_destino is None:
                continue

            # Solicitar unidad de distancia
            unidad = pedir_unidad()

            # Mostrar el resumen de confirmacion
            mostrar_resumen(
                datos_origen["nombre"],
                datos_destino["nombre"],
                unidad
            )

            # Mostrar las coordenadas obtenidas
            mostrar_coordenadas(datos_origen, datos_destino)

           
        
            # Calcular la distancia en kilometros
            distancia_km = calcular_distancia(
                datos_origen["lat"],
                datos_origen["lon"],
                datos_destino["lat"],
                datos_destino["lon"]
            )

            # Convertir la distancia a millas
            distancia_millas = round(distancia_km * 0.621371, 2)

            # Seleccionar la unidad que eligio el usuario
            if unidad == "millas":
                distancia = distancia_millas
            else:
                distancia = distancia_km

            # Mostrar el resultado
            print("\n--- Resultado de la distancia ---")
            print(f"Distancia: {distancia} {unidad}")
         
            # Calcular los tiempos estimados de viaje
            tiempo_avion = distancia_km / VELOCIDAD_AVION
            tiempo_auto = distancia_km / VELOCIDAD_AUTO

            # Convertir los tiempos a horas y minutos
            tiempo_avion_formato = convertir_tiempo(tiempo_avion)
            tiempo_auto_formato = convertir_tiempo(tiempo_auto)

            # Mostrar los tiempos estimados
            print("\n--- Tiempos estimados de viaje ---")
            print(f"Tiempo en avion: {tiempo_avion_formato}")
            print(f"Tiempo en auto: {tiempo_auto_formato}")


            # Mostrar el resumen final del viaje
            print("\n========== RESUMEN DEL VIAJE ==========")
            print(f"Origen: {datos_origen['nombre']}, {datos_origen['pais']}")
            print(f"Destino: {datos_destino['nombre']}, {datos_destino['pais']}")

            # Mostrar las distancias en ambas unidades
            print(f"\nDistancia en linea recta: {distancia_km:,.2f} km")
            print(f"Distancia en millas: {distancia_millas:,.2f} millas")

            # Mostrar los tiempos estimados
            print(f"\nTiempo estimado en avion ({VELOCIDAD_AVION} km/h): {tiempo_avion_formato}")
            print(f"Tiempo estimado en auto ({VELOCIDAD_AUTO} km/h): {tiempo_auto_formato}")

            # Aclaracion sobre la distancia
            print("\n* La distancia es una aproximacion en linea recta.")
            print("=======================================")


        elif opcion == "2":
            print("\n¡Gracias por usar nuestra calculadora!")
            print("¡Buen viaje turista!")
            break

        else:
            print("Error: Opción no válida. Intenta nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()

