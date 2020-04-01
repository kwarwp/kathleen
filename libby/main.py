# kathleen.libby.main.py
from _spy.vittolino.main import Cena,Elemento,Labirinto
from _spy.vittolino.main import INVENTARIO as inv
ANA_MARIA= "http://lorempixel.com/800/600/people/1"
DR_ZUCKMAN= "http://lorempixel.com/800/600/people/2"
COFRE= "http://lorempixel.com/800/600/city"
LABORATORIO= "http://lorempixel.com/800/600/city"
HOSPITAL= "http://lorempixel.com/800/600/city/2"
BIBLIOTECA= "http://lorempixel.com/800/600/city/3"
LAB_INFORMATICA= "http://lorempixel.com/800/600/city/4"
SALA1= "img norte LABORATORIO"
SALA2= "img leste HOSPITAL"
SALA3= "img oeste BIBLIOTECA"
SALA4= "img sul LAB_INFORMATICA"
class HAHA():
    def __init__(self): 
        anamaria=Elemento(img=ANA_MARIA)
        drzuckman= Elemento(img=DR_ZUCKMAN)
        cofre= Elemento(img=COFRE)
        laboratorio= Cena(img=LABORATORIO)
        hospital= Cena(img=HOSPITAL)
        biblioteca= Cena(img=BIBLIOTECA)
        labinformatica= Cena(img=LAB_INFORMATICA)
        hehe= LABIRINTO (norte= SALA1,leste= SALA2,oeste= SALA3,sul= SALA4)
        ana_maria.entra(hehe.norte)
        dr_zuckman.entra(hehe.norte)
        hehe.norte.vai()

HAHA()