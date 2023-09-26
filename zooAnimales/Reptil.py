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
    def cantidadReptiles (cls):
        return len(cls._listado)
    
    def crearIguana (cls, nombre, edad, genero):
        cls.iguanas +=1
        Reptil(nombre, edad, "humedal", genero, "verde", 3)

    def crearSerpiente (cls, nombre, edad, genero):
        cls.serpientes +=1
        Reptil(nombre, edad, "jungla", genero, "blanco", 1)