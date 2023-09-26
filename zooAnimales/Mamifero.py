from zooAnimales import Animal 
class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje 
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos (cls):
        return len(cls._listado)
    
    def crearCaballos(cls, nombre, edad, genero):
        cls.caballos +=1
        Mamifero(nombre, edad, "pradera", genero, True, 4)
        
    
    def crearLeon(cls, nombre, edad, genero):
        cls.leones +=1
        Mamifero(nombre, edad, "selva", genero, True, 4)
        
    