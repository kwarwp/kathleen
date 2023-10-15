# kathleen.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
INICIO="https://imgur.com/yJuD0vq"

class vai():
    inicio=Cena(img=INICIO)
    npc=Elemento(img="https://imgur.com/GbnwrWN", tit="NPC: Acabamos de receber uma mensagem da NASA informando que um dos satélites no espaço detectou um objeto no interior de um núcleo de gelo na região antártica.")
    npc.entra(inicio)
    inicio.vai()
vai()    