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
    def movimiento(cls):
        return "desplazarse"

    @classmethod
    def totalPorTipo (cls):
         return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def toString(self):
        if self._zona != None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el zoo " + self._zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad=edad

    def getHbaitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat=habitat
    
    def getGnero(self):
        return self._genero
    
    def setNombre(self, genero):
        self._genero=genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona=zona


    

    
