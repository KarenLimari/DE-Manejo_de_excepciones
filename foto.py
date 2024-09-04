from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.ancho = ancho #LLama al setter"ancho"
        self.alto = alto    #LLama al setter de "alto"
        self.ruta = ruta    #Asignación de la ruta de la foto

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho >self.MAX:
            raise DimensionError("Ancho fuera de rango", ancho, self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto > self.MAX:
            raise DimensionError("Alto fuera de rango", alto, self.MAX) 
        self.__alto = alto


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