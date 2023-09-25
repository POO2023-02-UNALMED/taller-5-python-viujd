from gestion import Zona
class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion 
        self._zonas= []

    def cantidadTotalAnimales (self):
        totalAni = 0
        for zona in self._zona:
            totalAni += zona.cantidadAnimales()
        return totalAni
    def agregarZonas (self, Zona):
        self._zonas.append(Zona)
    
