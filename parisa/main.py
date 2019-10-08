# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala
from _spy.vittolino.main import INVENTARIO as inv
SALA1 = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
SALA2 = "http://www.colegiohoje.com.br/img/predioEscola.png"
SALA3 = "https://cdn.pixabay.com/photo/2017/04/07/19/16/infinity-blue-2211659_960_720.jpg"
SALA4 = "https://cdn.pixabay.com/photo/2017/04/22/00/14/universe-2250310_960_720.jpg"
class OI():
    def __init__(self):
        sala1 = Cena(img = SALA1)
        mensagens=Codigo(cena=sala1, topo="Olá, nesse jogo você irá lidar com varios desafios........ TERMINAR A CONSTRUÇÃO", codigo="lorem ipsum sic dolor") 
        #sala1.vai()
        mensagens.vai()
        sala2 = Cena(img = SALA2)
        sala3 = Cena(img = SALA3)
        sala4 = Cena(img = SALA4)
        #sala4.vai()

        self.todos = todos = Sala( n= SALA1, s= SALA2, l= SALA3, o= SALA4)
        todos.norte.vai()
       
   
OI()
