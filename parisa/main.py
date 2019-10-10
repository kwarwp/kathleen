# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala
from _spy.vittolino.main import INVENTARIO as inv
SALA1 = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
SALA2 = "http://www.colegiohoje.com.br/img/predioEscola.png"
SALA3 = "https://estaticos.globoradio.globo.com/fotos/2018/05/6eb89bac-521f-4bac-b3a9-8a664831f478.jpg.640x360_q75_box-0%2C49%2C640%2C408_crop_detail.jpg"
SALA4 = "https://cdn.pixabay.com/photo/2017/04/22/00/14/universe-2250310_960_720.jpg"
class OI():
    def __init__(self):
        self.todos = todos = Sala( n= SALA1, s= SALA3, l= SALA2, o= SALA4)
        todos.norte.vai()
        mensagens= Codigo(cena=todos.norte, topo="Olá, nesse jogo você irá lidar com varios desafios........ TERMINAR A CONSTRUÇÃO", codigo="lorem ipsum sic dolor") 
        mensagens.vai()

   
OI()
