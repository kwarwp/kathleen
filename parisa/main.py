# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo
from _spy.vittolino.main import INVENTARIO as inv
INICIO = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
SALA1 = "http://www.colegiohoje.com.br/img/predioEscola.png"
class OI():
    inicio = Cena(img = INICIO)
    mensagens=Codigo(cena=inicio, topo="Olá, nesse jogo você irá lidar com varios desafios........ TERMINAR A CONSTRUÇÃO", codigo="lorem ipsum sic dolor") 
    inicio.vai()
    mensagens.vai()
    
    sala1 = Cena(img = SALA1)
    sala1.vai()
    
    todos = Labirinto( n= SALA1, s= SALA2, o = SALA3, l= SALA4)
    todos = Labirinto(l= SALA4, o= SALA5, n= SALA1)
OI()
