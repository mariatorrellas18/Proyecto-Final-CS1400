
# Proyecto Final CS1400 - Calculadora de Distancias
# Nombre: Gabriela Torrellas y Grecia Lopez


from utils import calcular_distancia
# Clase para representar una ciudad
class Ciudad:
    """
    Representa una ciudad con su nombre, pais
    y coordenadas geograficas.
    """

    # Constructor de la clase
    def __init__(self, nombre, pais, latitud, longitud):
        """Inicializa los atributos de una ciudad."""
        self.nombre = nombre
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud

    # Metodo para mostrar la informacion de la ciudad
    def __str__(self):
        """Devuelve la informacion de la ciudad como texto."""
        return (
            f"{self.nombre}, {self.pais} "
            f"({self.latitud:.2f}, {self.longitud:.2f})"
        )


    # Metodo para calcular la distancia a otra ciudad
    def distancia_a(self, otra):
        """
        Calcula la distancia entre esta ciudad y otra.
        Utiliza la formula de Haversine de utils.py.
        Devuelve la distancia en kilometros.
        """

        return calcular_distancia(
            self.latitud,
            self.longitud,
            otra.latitud,
            otra.longitud
        )
