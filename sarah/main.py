# kathleen.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
#from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
INICIO = "https://i.imgur.com/vFALZ8K.jpg"
class terror():
	#def __init__(self):
    npc=Elemento(img="https://i.imgur.com/GbnwrWN.png", style=dict(left=370, top=300, width=300, height="200px")) 
    inicio=Cena(img=INICIO)
    npc.entra(inicio)
    Texto(inicio, "NPC: Acabamos de receber uma mensagem da NASA informando que um dos satélites no espaço detectou um objeto no interior de um núcleo de gelo na região antártica").vai()
    
    inicio.vai()
terror()
class oi():
    Texto(inicio, "Sua missão é encontrá-lo! Mas antes você precisará fazer algumas escolhas.").vai()
oi()