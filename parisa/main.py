# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo
from _spy.vittolino.main import INVENTARIO as inv
SALA1 = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
SALA2 = "http://www.colegiohoje.com.br/img/predioEscola.png"
class OI():
    sala1 = Cena(img = SALA1)
    mensagens=Codigo(cena=inicio, topo="Olá, nesse jogo você irá lidar com varios desafios........ TERMINAR A CONSTRUÇÃO", codigo="lorem ipsum sic dolor") 
    sala1.vai()
    mensagens.vai()
    
    sala2 = Cena(img = SALA2)
    sala2.vai()
    
    todos = Labirinto( n= SALA1, s= SALA2)
    
   
OI()
