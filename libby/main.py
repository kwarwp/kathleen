# kathleen.libby.main.py
from _spy.vittolino.main import Cena,Elemento,Labirinto
from _spy.vittolino.main import INVENTARIO as inv
ANA_MARIA= "
DR_ZUCKMAN= "
COFRE= "
LABORATORIO= "
HOSPITAL= "
BIBLIOTECA= "
LAB_INFORMATICA= "
SALA1= "img norte LABORATORIO"
SALA2= "img leste HOSPITAL"
SALA3= "img oeste BIBLIOTECA"
SALA4= "img sul LAB_INFORMATICA"
Class HAHA():
init_main (self)
ana_maria= Elemento(img ANA_MARIA)
dr_zuckman= Elemento(img DR_ZUCKMAN)
cofre= Elemento(img COFRE)
laboratorio= Cena(img LABORATORIO)
hospital= Cena(img HOSPITAL)
biblioteca= Cena(img BIBLIOTECA)
lab_informatica= Cena(img LAB_INFORMATICA)
hehe= LABIRINTO (norte= SALA1,leste= SALA2,oeste= SALA3,sul= SALA4)
ana_maria.entra(hehe.norte)
dr_zuckman.entra(hehe.norte)
hehe.norte.vai()

HAHA()