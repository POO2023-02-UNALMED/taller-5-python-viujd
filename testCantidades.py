from gestion.lonar import Zona
from gestion.loogico import Zoologico 
from zooAnimales.dangio import Anfibio
from zooAnimales.dahe import Ave
from zooAnimales.kakiero import Mamifero
from zooAnimales.ress import Pez
from zooAnimales.pedil import Reptil
from zooAnimales.calima import Animal

zoo = Zoologico("Zoologico Central", "Chicago")
z1 = Zona("zona1")
z2 = Zona("zona2")
zoo.agregarZonas(z1)
zoo.agregarZonas(z2)
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearLeon("test", 11, "M"))
z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
z1.agregarAnimales(Anfibio.crearRana("test", 11, "M"))
z2.agregarAnimales(Anfibio.crearSalamandra("test", 11, "M"))
z2.agregarAnimales(Reptil.crearIguana("test", 11, "M"))
z2.agregarAnimales(Reptil.crearSerpiente("test", 11, "M"))
z2.agregarAnimales(Pez.crearSalmon("test", 11, "M"))
z2.agregarAnimales(Pez.crearBacalao("test", 11, "M"))
Mamifero.crearCaballo("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
Anfibio.crearRana("test", 11, "M")
Reptil.crearIguana("test", 11, "M")
Pez.crearBacalao("test", 11, "M")

def testCantidadAnimales():
    ok = False
    if zoo.cantidadTotalAnimales() == 13:
        ok = True
    assert(ok)

def testCantidadAnimalesZonas():
    ok = False
    if zoo.getZona()[0].cantidadAnimales() == 8:
        ok = True
    assert(ok)

def testCantidadMamiferos():
    ok = False
    if Mamifero.caballos == 3 and Mamifero.leones == 1:
        ok = True
    assert(ok)

def testCantidadAves():
    ok = False
    if Ave.aguilas == 2 and Ave.halcones ==3:
        ok = True
    assert(ok)

def testCantidadAnfibios():
    ok = False
    if Anfibio.ranas == 2 and Anfibio.salamandras == 1:
        ok = True
    assert(ok)

def testCantidadReptiles():
    ok = False
    if Reptil.iguanas == 2 and Reptil.serpientes == 1:
        ok = True
    assert(ok)

def testCantidadPeces():
    ok = False
    if Pez.salmones == 1 and Pez.bacalaos == 2:
        ok = True
    assert(ok)