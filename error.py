class DimensionError (Exception):
    def __init__(self,mensaje, dimension, maximo):
        super().__init__()
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    