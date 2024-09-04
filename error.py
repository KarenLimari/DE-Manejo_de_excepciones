class DimensionError (Exception):
    """
    Excepción personalizada para manejar errores relacionados con las dimensiones.

    Esta excepción se utiliza para indicar que un valor de dimensión (ancho o alto) está fuera del rango permitido.

    Attributes
    ----------
    mensaje : str
        Mensaje de error proporcionado al crear la excepción.
    dimension : int, optional
        Valor recibido que está fuera del rango permitido (default es None).
    maximo : int, optional
        Valor máximo permitido para la dimensión (default es None).
    """
    #constructor
    def __init__(self,mensaje, dimension = None, maximo = None):
        """
        Inicializa una nueva instancia de DimensionError.

        Parameters
        ----------
        mensaje : str
            Mensaje de error que describe el problema.
        dimension : int, optional
            Valor de dimensión que causó el error (default es None).
        maximo : int, optional
            Valor máximo permitido para la dimensión (default es None).
        """
        super().__init__(mensaje)   #LLama al constructo de la clase base Exception
        self.mensaje = mensaje      #Almacena el mensaje del error
        self.dimension = dimension  #Almacena el valor de la dimensión que causó el error
        self.maximo = maximo        #Almacena el valor máximo permitido para la dimensión

    def __str__(self):
        """
        Devuelve una representación en cadena del error.

        Returns
        -------
        str
            Mensaje de error detallado que incluye el mensaje, el valor recibido y el máximo permitido.
        """
        if self.dimension is None or self.maximo is None:
            #Si dimension o máximo son None, devuelve el mensaje de error de la clase base.
            return super().__str__()
        #Devuelve el mensaje detallado con el mensaje, valor recibido y el máximo permitido.
        return f"{self.mensaje}, valor recibido:{self.dimension}, máximo permitido:{self.maximo}"