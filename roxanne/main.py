# kathleen.roxanne.main.py
from _spy.vitollino.main import Cena, Texto, STYLE,Sala
from _spy.vitollino.main import INVENTARIO as inv
from elemento.main import Elemento 
STYLE["width"] = 800
STYLE["height"] = "600px"


LABORATORIO = "http://lorempixel.com/800/600/city"
ANA_MARIA = "http://lorempixel.com/800/600/people/1"
DR_ZUKMAN = "http://lorempixel.com/800/600/people/2"
PORTA = "http://lorempixel.com/800/600/city/5"
HOSPITAL = "http://lorempixel.com/800/600/city"
COFRE = "http://lorempixel.com/800/600/city"
PAPEIS = "http://lorempixel.com/800/600/city"
SALA1= "http://lorempixel.com/800/600/city/1"
SALA2= "http://lorempixel.com/800/600/city/2"
SALA3= "http://lorempixel.com/800/600/city/3"
SALA4= "http://lorempixel.com/800/600/city/4"
PERSONAGEM = None

class doidera():
    def __init__(self):
        #laboratorio= Cena(img=LABORATORIO)
        pass
class Personagens():
    def __init__(self):
        self.ana_maria= Elemento(img=ANA_MARIA, tit="Aninha", drag=True, style=dict(
            left=100, top=10, width=60, height="60px")) 
        dr_zukman=Elemento(img=DR_ZUKMAN, style=dict(
            left=200, top=10, width=60, height="60px")) 
    def some(self):
        self.ana_maria.entra(Cena())
    def entra(self,lugar):
        self.ana_maria.entra(lugar)
class Porta(): 
    def __init__(self):
        dragger=dict(Aninha=self.entra_porta)
        self.porta=Elemento(img=PORTA,tit="portela", drop=dragger, style=dict(
            left=10, top=10, width=60, height="60px"))
    def entra (self,lugar):
        self.porta.entra(lugar)
    def entra_porta(self,evento,nome):
        PERSONAGEM.some()
class Cenas():
    def __init__(self): 

        self.congresso= congresso = Sala(n=SALA1,l=SALA2,o= SALA3, s=SALA4)
        PERSONAGEM.entra(congresso.norte)
        # dr_zukman.entra(congresso.norte)
        Porta().entra(congresso.norte)
        congresso.norte.vai()
    def entra_porta(self,evento,nome):
        PERSONAGEM.some()
PERSONAGEM=Personagens()
Cenas()
#doidera()

    
    

