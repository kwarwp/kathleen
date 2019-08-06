# kathleen.roxanne.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE,Sala
from _spy.vitollino.main import INVENTARIO as inv

LABORATORIO = "lorempixel.com/800/600/city"
ANA_MARIA = "lorempixel.com/800/600/people"
DR_ZUKMAN = "lorempixel.com/800/600/people"
PORTA = "lorempixel.com/800/600/city"
HOSPITAL = "lorempixel.com/800/600/city"
COFRE = "lorempixel.com/800/600/city"
PAPEIS = "lorempixel.com/800/600/city"
SALA1= "lorempixel.com/800/600/city"
SALA2= "lorempixel.com/800/600/city"
SALA3= "lorempixel.com/800/600/city"
SALA4= "lorempixel.com/800/600/city"


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

    
    

