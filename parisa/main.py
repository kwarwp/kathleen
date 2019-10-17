# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
#inicio
SALA1 = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
#fachada da escola CENA 1
SALA2 = "https://i.pinimg.com/originals/4e/35/2c/4e352c35cc8b7c437ca26f3dfcc887a7.jpg"
#Sala de aula CENA 2
SALA3 = "https://st3.depositphotos.com/5383684/15265/v/1600/depositphotos_152658382-stock-illustration-in-front-of-empty-classroom.jpg"
#Corredor da escola CENA 4
SALA4 = "https://cdn.pixabay.com/photo/2014/08/13/20/16/school-417612_960_720.jpg"
#Quadra de esportes
SALA5 = "https://i.pinimg.com/originals/78/99/c9/7899c925ee95618ef0bd21f4b067175b.jpg"
MENINO= "https://cdn.pixabay.com/photo/2017/07/07/03/21/child-2480290_960_720.png"
LOGO= "http://supygirls.pythonanywhere.com/image/camisasuperpython.png"
#diretora neide RASCUNHO
NEIDE="https://i.pinimg.com/originals/25/48/27/254827fb621ed6c9e50b401d92554810.png"
class OI():
    def __init__(self):
        self.todos = todos = Sala( n= SALA1, s= SALA3, l= SALA2, o= SALA4)
        todos.norte.vai()
        #self.todos = todos = Sala( o= SALA4, s=SALA5, l=SALA6, n=SALA1)
        #todos.norte.vai()
        logo = Elemento(img=LOGO, style=dict(left=370, top=200, width=450, height="250px"))
        logo.entra(todos.norte)
        falalogo=Texto(todos.norte,"O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão. ")
        logo.vai=falalogo.vai
        
        neide=Elemento(img=NEIDE, style=dict(left=100, top=350, width=300, height="200px"))
        neide.entra(todos.leste)
        falaneide= Texto(todos.leste, "Seja bem vindo! Esse é o Colégio _______ e estamos contentes em recebe-lo, espero que se adapte a sua nossa vida acadêmica.")
        neide.vai=falaneide.vai
        
        menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        menino.entra (todos.leste)
        falamenino= Texto(todos.leste, "Muito obrigado, Senhora Neide")
        menino.vai=falamenino.vai
        
        
        
        
       # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
        #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
        #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
       # mensagens.vai()
       ##[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
