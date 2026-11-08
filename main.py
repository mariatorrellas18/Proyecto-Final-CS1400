"""
Bienvenida a nuestro proyecto final de CS1400, donde exploraremos y aplicaremos los conceptos aprendidos a lo largo del curso.
- Gabriela Torrellas y Grecia Lopez.
"""

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


# Funcion para mostrar el resumen
def mostrar_resumen(origen, destino, unidad):
    """Muestra un resumen de los datos ingresados."""
    print("\n--- Resumen ---")
    print(f"Origen:  {origen}")
    print(f"Destino: {destino}")
    print(f"Unidad:  {unidad}")
    print("Consultando datos...")


# Funcion principal del programa
def main():
    """Ejecuta el programa hasta que el usuario elija salir."""

    while True:
        mostrar_menu()

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print()

            # Solicitar origen y destino
            origen = pedir_ciudad("Ciudad de origen: ")
            destino = pedir_ciudad("Ciudad de destino: ")

            # Solicitar unidad de distancia
            unidad = pedir_unidad()

            # Mostrar el resumen de confirmacion
            mostrar_resumen(origen, destino, unidad)

        elif opcion == "2":
            print("\n¡Gracias por usar nuestra calculadora!")
            print("¡Buen viaje!")
            break

        else:
            print("Error: Opción no válida. Intenta nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
