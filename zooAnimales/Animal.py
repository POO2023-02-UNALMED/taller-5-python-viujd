import zooAnimales
class Animal:
    _totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero):
        
        self._nombre = nombre
        self._edad = edad
        self._habitat= habitat
        self._genero = genero
        self._zona= None
        Animal._totalAnimales +=1

    @classmethod
    def totalPorTipo (cls):
         return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
   