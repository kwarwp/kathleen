# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
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
#diretora neide RASCUNHO
NEIDE="https://i.pinimg.com/originals/25/48/27/254827fb621ed6c9e50b401d92554810.png"
class OI():
    def __init__(self):
        self.todos = todos = Sala( n= SALA1, s= SALA3, l= SALA2, o= SALA4)
        todos.norte.vai()
        
        logo = Elemento(img=LOGO, style=dict(left=370, top=200, width=450, height="250px"))
        logo.entra(todos.norte)
        falalogo=Texto(todos.norte,"O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa bárbarie, e, saber o limite de brincadeira e agressão. ")      logo.vai=falalogo.vai
        
        neide=Elemento(img=NEIDE, style=dict(left=100, top=350, width=300, height="200px"))
        neide.entra(todos.leste)
        falaneide= Texto(todos.leste, "Seja bem vindo!")
        neide.vai=falaneide.vai
        
        
       # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
        #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
        #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
       # mensagens.vai()
       ##[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
