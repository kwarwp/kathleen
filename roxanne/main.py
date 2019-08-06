# kathleen.roxanne.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE,Sala
from _spy.vitollino.main import INVENTARIO as inv

LABORATORIO = "lorenpixel.com/800/600/city"
ANA_MARIA = "lorenpixel.com/800/600/people"
DR_ZUKMAN = "lorenpixel.com/800/600/people"
PORTA = "lorenpixel.com/800/600/city"
HOSPITAL = "lorenpixel.com/800/600/city"
COFRE = "lorenpixel.com/800/600/city"
PAPEIS = "lorenpixel.com/800/600/city"
SALA1= "lorenpixel.com/800/600/city"
SALA2= "lorenpixel.com/800/600/city"
SALA3= "lorenpixel.com/800/600/city"
SALA4= "lorenpixel.com/800/600/city"


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
        
doidera()

    
    

