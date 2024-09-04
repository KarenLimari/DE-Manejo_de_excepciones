from error import DimensionError

class Foto():
    """
    Clae para representar una foto con dimensiones controladas.

    Atributos:

    MAX :int
        Valor máximo permitifo para ancho y alto dela foto.

    """
    MAX = 2500  #Valor máximo permitido para el ancho y alto de la foto.

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Inicializa una nueva instancia de la clase Foto.

        Parámetros
        ----------
        ancho : int
            Ancho de la foto.
        alto : int
            Alto de la foto.
        ruta : str
            Ruta del archivo de la foto.
        """
        
        self.ancho = ancho #LLama al setter"ancho"
        self.alto = alto    #LLama al setter de "alto"
        self.ruta = ruta    #Asignación de la ruta de la foto

    @property
    def ancho(self) -> int:
        """
        Devuelve el ancho de la foto.

        Returns
        -------
        int
            Ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        """
        Establece el ancho de la foto, verificando que esté dentro del rango permitido.

        Parámetros
        ----------
        ancho : int
            Nuevo valor para el ancho de la foto.

        Raises
        ------
        DimensionError
            Si el ancho está fuera del rango permitido (1 <= ancho <= MAX).
        """
        if ancho < 1 or ancho >self.MAX:
            raise DimensionError("Ancho fuera de rango", ancho, self.MAX)
        self.__ancho = ancho    # Asigna el valor de ancho si está dentro del rango permitido

    @property
    def alto(self) -> int:
        """
        Devuelve el alto de la foto.

        Returns
        -------
        int
            Alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        """
        Establece el alto de la foto, verificando que esté dentro del rango permitido.

        Parámetros
        ----------
        alto : int
            Nuevo valor para el alto de la foto.

        Raises
        ------
        DimensionError
            Si el alto está fuera del rango permitido (1 <= alto <= MAX).
        """
        if alto < 1 or alto > self.MAX:
            raise DimensionError("Alto fuera de rango", alto, self.MAX) 
        self.__alto = alto  # Asigna el valor de alto si está dentro del rango permitido


if __name__ == "__main__":
    try:
        # Ejemplo: una foto dentro del rango.
        foto1 = Foto(ancho=1500, alto=2000, ruta="foto1.jpg")
        print(f"Foto 1 creada con éxito: ancho={foto1.ancho}, alto={foto1.alto}")

        # Intentar crear una foto fuera del rango
        foto2 = Foto(ancho=3000, alto=3000, ruta="foto2.jpg")  # Debería lanzar una excepción
        print(f"Foto 2 creada con éxito: ancho={foto2.ancho}, alto={foto2.alto}")
    except DimensionError as e:
        print(f"Se produjo un error: {e}")