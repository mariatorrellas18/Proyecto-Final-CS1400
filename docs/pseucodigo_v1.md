Para nuestro proyecto final CS1400
Estamos realizando esta calculadora de distancias, esta calculadora permite al usuario ingresar una ciudad de origen, una ciudad de destino y elegir si quiere la distancia en kilómetros o millas. 

Comenzamos con la primera Función: 
#mostrar_menu()
Primero, creamos una función llamada mostrar_menu() que se encarga de mostrar la bienvenida al turista y las opciones disponibles. Utilizamos def para definir la función y print() para mostrar los mensajes en pantalla. El usuario tiene dos opciones, puede elegir entre calcular una distancia o salir del programa.

#Función pedir_ciudad()
Esta función nos permite pedir al usuario la ciudad de origen y la ciudad de destino. Utilizamos input() para recibir la información y .strip() para eliminar los espacios innecesarios al principio y al final del texto.

También usamos while True para repetir la pregunta si el usuario deja el campo vacío. Con if verificamos que haya escrito una ciudad y con return devolvemos el nombre. Si no escribe nada, else muestra un mensaje de error.

#Función pedir_unidad()
Esta función permite elegir en qué unidad queremos calcular la distancia, ya sea kilómetros o millas.

Usamos input(): para recibir la respuesta, .strip() para quitar espacios y .lower() para convertir el texto a minúsculas y evitar problemas si el usuario escribe con mayúsculas.

Utilizamos if y elif: para comprobar si escribió "km" o "millas". Si la respuesta es correcta, usamos return para devolver la unidad seleccionada. Si escribe algo diferente, else muestra un error y el programa vuelve a preguntar gracias a while True.

#Función mostrar_resumen()
Esta función se encarga de mostrar un resumen de la información que ingresó el usuario.

Recibe tres datos: origen, destino y unidad. Utilizamos print() para mostrar las ciudades seleccionadas y la unidad de distancia.

También usamos f antes de las comillas para incluir los valores de las variables dentro de los mensajes, como f"Origen: {origen}".

Al final, mostramos el mensaje "Consultando datos..." para indicar que estamos preparando la consulta.

#Función main()
Esta es la función principal porque se encarga de controlar todo el funcionamiento del programa.

Primero, utilizamos while True para que el menú se siga mostrando hasta que el usuario decida salir.

Llamamos a mostrar_menu() para enseñar las opciones y usamos input() para pedir que elija una.

Si selecciona la opción 1, utilizamos if para llamar a las funciones pedir_ciudad(), pedir_unidad() y mostrar_resumen(). Así podemos obtener la información y mostrarla de forma organizada.

Si selecciona la opción 2, utilizamos elif para mostrar un mensaje de despedida y break para terminar el ciclo y salir del programa.

Si escribe una opción incorrecta, usamos else para mostrar un mensaje de error y permitirle intentar nuevamente.

#Ejecución del programa
Finalmente, utilizamos if __name__ == "__main__": para indicar que la función main() debe ejecutarse cuando abrimos directamente este archivo de Python.

Esto permite que el programa comience mostrando el menú principal.