from zooAnimales import Animal 
class Pez(Animal):
    _listado= []
    salmones = 0
    bacalao = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)