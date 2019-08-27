# kathleen.stacy.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv

from roxanne.main import doidera 

STYLE["width"] = 800
STYLE["height"] = "600px"


ESTAGIARIO = "http://lorempixel.com/800/600/people/3"
GARCA1  = "http://lorempixel.com/800/600/people/4"
GARCA2  = "http://lorempixel.com/800/600/people/5"
GARCA3 = "http://lorempixel.com/800/600/people/6"



class alunos():
    def __init__ (self):
        congresso = doidera().congresso
        estagiario = Elemento(img=ESTAGIARIO, style=dict(left=100, top=10, width=60, height="60px"))
        estagiario.entra(congresso.norte)
        garca1 = Elemento(img=GARCA1, tit="modificada", style=dict(left=102, top=11, width=60, height="60px")) 
        garca2 = Elemento(img=GARCA2, tit="modificada", style=dict(left=90, top=12, width=60, height="60px")) 
        garca3 = Elemento(img=GARCA3, tit="modificada", style=dict(left=109, top=15, width=60, height="60px")) 
        garca1.entra(congresso.norte)
        garca2.entra(congresso.norte)
        garca3.entra(congresso.norte)
        congresso.norte.vai()

  
alunos()