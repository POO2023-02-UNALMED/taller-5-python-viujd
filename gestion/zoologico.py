class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion 
        self._zonas= []

    def cantidadTotalAnimales (self):
        totalAni = 0
        for zona in self._zonas:
            totalAni += zona.cantidadAnimales()
        return totalAni
    def agregarZonas (self, Zona):
        self._zonas.append(Zona)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre=nombre

    def getUbicacion (self):
        return self._ubicacion
    
    def setUbicacion (self, ubicacion):
        self._ubicacion=ubicacion
    
    def getZona(self):
        return self._zonas
        
    def setZona(self, zonas):
        self._zonas=zonas
