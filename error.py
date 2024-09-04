class DimensionError (Exception):
    #constructor
    def __init__(self,mensaje, dimension = None, maximo = None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None or self.dimension is None:
            return super().__str__()
        
        return f"{self.mensaje}, valor recibido:{self.dimension}, máximo permitido:{self.maximo}"