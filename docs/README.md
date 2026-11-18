# Proyecto: Calculadora de Distancias

## Descripción del proyecto

En este proyecto, Gabriela y yo Grecia, estamos trabajando en una calculadora de distancias que permite ingresar una ciudad de origen y una ciudad de destino para saber qué tan lejos están una de la otra. También agregamos la opción de elegir si queremos ver la distancia en kilómetros o millas

Para hacer el programa fuimos utilizando diferentes funciones de Python para organizar mejor el codigo y hacer que cada parte tuviera su propio trabajo 

# Archivo main.py

En main.py trabajamos en la parte principal del programa. Creamos varias funciones para que el usuario pueda ingresar el origen (donde se encuentra actialmente), y  destino (a donde quiere llegar esa persona) y ver los resultados y cuanta distancia esta ya sea millas o en kilometros

Algunas de las funciones que utilizamos son para nuestra calculadora de distancia es:

 mostrar_menu(): muestra las opciones del programa
 pedir_ciudad(): pide al usuario que escriba las ciudades
 pedir_unidad(): permite elegir entre kilómetros y millas 
 consultar_ciudad(): comprueba que las ciudades existan
 mostrar_coordenadas(): muestra la latitud y longitud de cada ciudad
 mostrar_resumen(): enseña la información y los resultados
 main()`: conecta todas las funciones para que el programa funciones

 También utilizamos if, elif y else para tomar decisiones, while para repetir preguntas y try y except para manejar errores. De esta manera, si ocurre algún problema, el programa puede seguir funcionando sin cerrarse inesperadamente.

 # Archivo api.py

En api.py trabajamos con dos funciones principales que nos ayudan a buscar las ciudades y calcular la distancia entre ellas

# obtener_coordenadas()

Esta función sirve para buscar una ciudad utilizando la API de Open-Meteo utilizamos requests para conectarnos a internet y solicitar la información de la ciudad

Tambien usamos requests.get() para hacer la consulta, timeout=10 para limitar el tiempo de espera y respuesta.json() para obtener los datos

Después verificamos si encontramos la ciudad y utilizamos return para devolver su nombre, país, latitud y longitud. También agregamos try y except para manejar posibles errores de conexión

# calcular_distancia() Math

Esta función se encarga de calcular la distancia entre las dos ciudades. Para hacerlo utilizamos la biblioteca math y la fórmula de Haversine, que permite calcular distancias utilizando las coordenadas geográficas.

Usamos math.radians() para convertir las coordenadas, diferentes operaciones matemáticas para obtener la distancia y una condición if para convertir el resultado a millas si esa es la opción seleccionada.

Al final utilizamos round() para redondear el resultado a dos decimales y return para enviar la distancia calculada a main.py

# Lo que hemos aprendido

Durante este proyecto, Gabriela y yo Grecia hemos aprendido a trabajar con diferentes funciones de Python y a organizar mejor nuestro código. Tambien aprendimos a conectar nuestro programa con una API para buscar información real de las ciudades y utilizar sus coordenadas para calcular distancias

Además, practicamos el uso de condiciones, ciclos, manejo de errores, módulos y operaciones matemáticas

Ha sido una buena oportunidad para poner en práctica lo que hemos aprendido en clase y entender cómo podemos unir diferentes partes de código para crear un programa que funciones