from gestion.lonar import Zona
from gestion.loogico import Zoologico 
from zooAnimales.dangio import Anfibio
from zooAnimales.dahe import Ave
from zooAnimales.kakiero import Mamifero
from zooAnimales.ress import Pez
from zooAnimales.pedil import Reptil
from zooAnimales.calima import Animal

def testTotalTipo():
    Anfibio.crearRana("test", 11, "M")
    Anfibio.crearSalamandra("test", 11, "M")
    Mamifero.crearCaballo("test", 11, "M")
    Mamifero.crearCaballo("test", 11, "M")
    Mamifero.crearLeon("test", 11, "M")
    Reptil.crearIguana("test", 11, "M")
    Pez.crearSalmon("test", 11, "M")
    Ave.crearHalcon("test", 11, "M")
    Ave.crearHalcon("test", 11, "M")
    ok = False
    comp = "Mamiferos : 3\nAves : 2\nReptiles : 1\nPeces : 1\nAnfibios : 2"
    print(comp.replace('\n', ''))
    print(Animal.totalPorTipo().replace('\n', ''))
    if Animal.totalPorTipo().replace('\n', '') == comp.replace('\n', ''):
        ok = True
    assert(ok)

def testToString():
    ave1 =Ave("paloma", 5, "ciudad", "F", "gris")
    ok = False
    comp = "Mi nombre es paloma, tengo una edad de 5, habito en ciudad y mi genero es F"
    if ave1.toString() ==  comp:
        ok = True
    assert(ok)