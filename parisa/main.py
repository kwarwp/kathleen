# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala
from _spy.vittolino.main import INVENTARIO as inv
#inicio
SALA1 = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
#fachada da escola CENA 1
SALA2 = "http://www.colegiohoje.com.br/img/predioEscola.png"
#Sala de aula CENA 2
SALA3 = "https://estaticos.globoradio.globo.com/fotos/2018/05/6eb89bac-521f-4bac-b3a9-8a664831f478.jpg.640x360_q75_box-0%2C49%2C640%2C408_crop_detail.jpg"
#Corredor da escola CENA 4
SALA4 = "https://cdn.pixabay.com/photo/2014/08/13/20/16/school-417612_960_720.jpg"
#Quadra de esportes
LOGO= "http://supygirls.pythonanywhere.com/image/camisasuperpython.png"
class OI():
    def __init__(self):
        logo = Elemento(img=LOGO, style=dict(left=100, top=150, width=200, height="150px"))
        
        self.todos = todos = Sala( n= SALA1, s= SALA3, l= SALA2, o= SALA4)
        todos.norte.vai()
        
        logo.entra(todos.norte)
        logo.vai()
        
        falalogo=Texto(norte,"O cientista foi sequetrado e roubaram as escrituras e seu compuatdor")
        logo.vai=falalogo.vai
       # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
        #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
        #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
       # mensagens.vai()
       ##[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
