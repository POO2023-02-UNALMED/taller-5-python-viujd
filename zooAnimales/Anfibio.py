from zooAnimales import Animal 
class Anfibio(Animal):
    _listado= []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel,  venenoso):
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios (cls):
        return len(cls._listado)
    
    def CrearRana (cls, nombre, edad, genero):
        cls.ranas +=1
        Anfibio(nombre, edad, "selva", genero, "rojo", True)

    def CrearSalamandra (cls , nombre, edad, genero ):
        cls.salamandras +=1
        Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)