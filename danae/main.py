# kathleen.danae.main.py
from _spy.vittolino.main import Cena, Elemento , Labirinto
from _spy.vittolino.main import inventario as inv
CIENTISTA=""
AJUDANTE=""
LABORATORIO=""
JARDIM=""
CAIXADEMUSICA=""
HOLOGRAMA=""
JOGADOR=""
HOSPITAL=""
ANTIDOTO=""
PAREDE=""
SETASFLORESCENTES=""
 class CLOCK():
    cientista= Elemento(img=CIENTISTA)
    ajudante= Elemento(img=AJUDANTE)
    caixinha= Elemento(img=CAIXADEMUSICA)
    jogador= Elemento(img=JOGADOR)
    holograma= Elemento(img=HOLOGRAMA)
    antidoto= Elemento(img=ANTIDOTO)
    setinhas= Elementos(img=SETASFLORESCENTES)
    laboratorio= Cena(img=LABORATORIO)
    jardim= Cena(img=JARDIM)
    hospital= Cena(img=HOSPITAL)
    parede= Cena(img=PAREDE)
    