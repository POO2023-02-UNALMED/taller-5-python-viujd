from zooAnimales import Animal 
class Pez(Animal):
    _listado= []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces (cls):
        return len(cls._listado)
    
    def crearSalmon (cls, nombre, edad, genero):
        cls.salmones +=1
        Pez(nombre, edad, "oceano", genero, "rojo", 6)

    def crearBacalao (cls, nombre, edad, genero):
        cls.bacalaos +=1
        Pez(nombre, edad, "oceano", genero, "gris", 6)