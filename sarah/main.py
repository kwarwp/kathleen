# kathleen.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vitollino.main import INVENTARIO as inv
INICIO = "https://i.imgur.com/vFALZ8K.jpg"
class terror():
    npc=Elemento(img="https://i.imgur.com/GbnwrWN.png" , tit = "NPC: Acabamos de receber uma mensagem da NASA informando que um dos satélites no espaço detectou um objeto no interior de um núcleo de gelo na região antártica")
    inicio=Cena(img=INICIO)
    npc.entra(inicio)
    inicio.vai()
terror()
    