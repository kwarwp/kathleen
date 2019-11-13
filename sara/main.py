# kathleen.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto
from _spy.vitollino.main import INVENTARIO as inv

ANA_MARIA="http://lorempixel.com/800/600/people/1"
DR_DUCKMAN="http://lorempixel.com/800/600/people/2"
LABORATORIO="http://lorempixel.com/800/600/city"
HOSPITAL="http://lorempixel.com/800/600/city"
SALA1="http://lorempixel.com/800/600/city"
SALA2="http://lorempixel.com/800/600/city"

class CHOCOLATE():
    #def __init__(self):
    ana_maria=Elemento(img=ANA_MARIA) 
    dr_duckman=Elemento(img=DR_DUCKMAN)
    laboratorio=Cena(img=LABORATORIO)
    hospital=Cena(img=HOSPITAL)
    sala1=Cena(img=SALA1)
    sala2=Cena(img=SALA2)
    ana_maria.entra(sala1)
    dr_duckman.entra(sala2)
    sala1.direita=sala2
    sala2.esquerda=sala1
    sala1.vai()        
CHOCOLATE() 