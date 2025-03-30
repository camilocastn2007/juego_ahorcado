import random

class Diccionario:
    """
    Representa un diccionario de palabras para el juego.

    Attributes:
        palabras (list[str]): Lista de palabras cargadas desde un archivo externo.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
        Carga las palabras desde un archivo de texto.

        Returns:
            list[str]: Lista de palabras disponibles en el diccionario.
        """
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())
        return palabras

    def obtener_palabra(self) -> str:
        """
        Selecciona y devuelve una palabra aleatoria del diccionario.

        Returns:
            str: Palabra seleccionada aleatoriamente.
        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]