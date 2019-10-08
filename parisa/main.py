# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto
from _spy.vittolino.main import INVENTARIO as inv
INICIO = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"

class OI():
inicio = Cena(img = INICIO)
MENSAGENS = [
          [ inicio, "Olá"]
          ]
      inicio.vai()
OI()
