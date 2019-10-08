# kathleen.meredith.main.py
from _spy.vitollino.main import Cena, Texto


class Opt:
    def __init__(self):
        self.c = c = Cena("http://lorempixel.com/400/200/")
        self.t = t = Texto(c,"vai?", A="Vai A", B="Vai B")
        t.mostra(c,"vai?", A="Vai A", B="Vai B")
        t.vai()
        self.f = f = Texto(c, t.POP.optou)
        c.vai()
        
Opt()
