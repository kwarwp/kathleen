# kathleen.meredith.main.py
from _spy.vitollino.main import Cena, Texto


class Opt:
    def __init__(self):
        self.c = c = Cena("http://lorempixel.com/400/200/")
        self.t = t = Texto(c,"vai?", A="Vai A", B="Vai B", foi=self.foi)
        t.mostra(c,"vai?", A="Vai A", B="Vai B")
        t.vai()
        c.vai()
        
    def foi(self, *_):
        Texto(self.c, t.POP.optou).vai()
        
        
Opt()
