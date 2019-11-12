# kathleen.grace.main.py
from _spy.vitollino.main import Cena,Elemento,Labirinto e Texto
from _spy.vitollino.main import INVENTARIO as inv
#STYLE=["width"] = 800
#STYLE=["height"] = "600px"


CHARLES=""
LABORATORIO=""
LABOTY=""
AJUDANTE=""
POLICIA=""
LIVRO=""
class bruninha ():
    laboratorio=Cena(img=LABORATORIO)
    livro=Cena(img=LIVRO)
    laboty=Cena(img=LABOTY)
    charles=Elemento(img=CHARLES)
    laboratorio.direita=laboty
    laboty.direita=livro
    livro.esquerda=laboty
    laboty.esquerda=laboratorio
    piranha=Elemento(img=PIRANHA)
    ines=Elemento(img=INES)
    ines.entra(igreja)
    falaines=Texto(igreja, "graças a Deus")
    ines.vai=falaines.vai
    coringa=Elemento(img=CORINGA)
    piranha.entra(espaco)
    coringa.entra(casadabarbie)
    espaco.vai()
bruninha()