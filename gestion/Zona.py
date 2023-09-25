from zooAnimales import Animales
class Zona:
    def __init__(self, nombre, zoo= None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, Animales):
        self._animales.append(Animales)

    def cantidadAnimales(self):
        return len(self._animales)
        
