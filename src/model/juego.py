from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes

class Juego:
    """
    Clase principal que gestiona el flujo del juego.
    """
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
        Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self) -> int:
        """
        Retorna la cantidad de intentos que el jugador ha realizado.
        
        :return: Número de intentos realizados.
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
        Retorna la instancia de Adivinanza actual.
        
        :return: Objeto de la clase Adivinanza.
        """
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
        Genera una palabra aleatoria desde el diccionario.
        
        :return: Palabra seleccionada.
        """
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        """
        Calcula la cantidad de intentos permitidos según la dificultad actual.
        
        :return: Número de intentos permitidos.
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5
        return 0
