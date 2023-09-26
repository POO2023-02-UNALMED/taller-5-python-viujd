from zooAnimales import Animal 
class Ave(Animal):
    _listado= []
    hacones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves (cls):
        return len(cls._listado)
    
    def crearHalcon (cls, nombre, edad, genero):
        cls.hacones +=1
        Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        
    def crearAguila (cls, nombre, edad, genero):
        cls.aguilas +=1
        Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    