from zooAnimales import Animal 
class Reptil(Animal):
    _listado= []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def movimiento(cls):
        return "reptar"

    @classmethod
    def cantidadReptiles (cls):
        return len(cls._listado)
    
    @classmethod
    def crearIguana (cls, nombre, edad, genero):
        cls.iguanas +=1
        Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente (cls, nombre, edad, genero):
        cls.serpientes +=1
        Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado=listado

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCOla(self, largoCola):
        self._largoCola= largoCola