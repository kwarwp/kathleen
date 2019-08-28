# kathleen.morgan.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto
from _spy.vitollino.main import Inventario as inv
ARENA = "https://i.pinimg.com/originals/79/42/7f/79427f813a3e0c39eb834ed07a7e96af.jpg"
KATNISS = "https://1.bp.blogspot.com/-uIYoL6p-M54/V1NLGwpwgYI/AAAAAAAAFPM/j5-M-jR7xdkyHTN6tgCp0DoT4TUF8ZuEwCKgB/s640/31.png"
class HGAMES():
      #def __ int __(self):
        arena = Cena ( img = ARENA )
        katniss = Elemento ( img = KATNISS )
        katniss.entra(arena)
        arena.vai()
HGAMES()