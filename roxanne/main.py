# kathleen.roxanne.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE,Sala
from _spy.vitollino.main import INVENTARIO as inv

LABORATORIO = "http://lorempixel.com/800/600/city"
ANA_MARIA = "http://lorempixel.com/800/600/people"
DR_ZUKMAN = "http://lorempixel.com/800/600/people"
PORTA = "http://lorempixel.com/800/600/city"
HOSPITAL = "http://lorempixel.com/800/600/city"
COFRE = "http://lorempixel.com/800/600/city"
PAPEIS = "http://lorempixel.com/800/600/city"
SALA1= "http://lorempixel.com/800/600/city"
SALA2= "http://lorempixel.com/800/600/city"
SALA3= "http://lorempixel.com/800/600/city"
SALA4= "http://lorempixel.com/800/600/city"


class doidera():
    def __init__(self):
        #laboratorio= Cena(img=LABORATORIO)
        ana_maria= Elemento(img=ANA_MARIA)
        dr_zukman=Elemento(img=DR_ZUKMAN)
        porta=Elemento(img=PORTA)
        congresso=Sala(n=SALA1,l=SALA2,o= SALA3, s=SALA4)
        ana_maria.entra(congresso.norte)
        dr_zukman.entra(congresso.norte)
        porta.entra(congresso.norte)
        congresso.norte.vai()
        
doidera()

    
    

