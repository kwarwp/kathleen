# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
#inicio
SALA1 = "https://www.loskatchorros.com.br/forum/uploads/monthly_2017_08/maxresdefault.jpg.3845d9d72470fe4e52aa779cf96871b5.jpg"
#fachada da escola CENA 1
SALA2 = "https://i.imgur.com/klmWAtd.png"
#Sala de aula CENA 2
SALA3 = "https://i.imgur.com/KGfgpSwr.jpg"
#Corredor da escola CENA 4
SALA4 = "https://i.imgur.com/0xs8URf.jpg"
#Quadra de esportes
SALA5 = "https://i.pinimg.com/originals/78/99/c9/7899c925ee95618ef0bd21f4b067175b.jpg"
#desconhecida 
SALA6 = "https://s3-sa-east-1.amazonaws.com/uploads-ntro/blog/wp-content/uploads/2017/04/06121758/sonhar-com-mar.jpg"
MENINO= "https://cdn.pixabay.com/photo/2017/07/07/03/21/child-2480290_960_720.png"
LOGO= "http://supygirls.pythonanywhere.com/image/camisasuperpython.png"
#diretora neide RASCUNHO
NEIDE="https://i.pinimg.com/originals/25/48/27/254827fb621ed6c9e50b401d92554810.png"
A= "https://i.imgur.com/BbqiLtF.jpg"
B= "https://i.imgur.com/V02Plm4.jpg"
C= "https://i.imgur.com/Brb4yHm.jpg"

class OI():
    def __init__(self):
    
        self.todos = todos = Sala(n= SALA1, l= SALA2, s= SALA3, o= SALA4)                      
        self.todas=todas= Sala(o= SALA4, s= SALA5, l= SALA6, n= SALA1)
        self.todos.oeste.vai=self.todas.sul.vai
        self.todas.leste.vai=self.todos.norte.vai
        self.todos.norte.vai
        self.todas.oeste.vai
        
        #self.todos.oeste.vai=self.todas.sul.vai
        #self.todas.todas.vai()
        #self.SALA4.direita=todas
        #todos.norte.vai()  
        #self.todos = todos = Sala( o= SALA4, s=SALA5, l=SALA6, n=SALA1)
        #todos.norte.vai()
        self.logo = Elemento(img=LOGO, style=dict(left=370, top=200, width=450, height="250px"))
        self.logo.entra(todos.norte)
        self.falalogo=Texto(todos.norte,"O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbaridade, e saber o limite de brincadeira e agressão. ")
        self.logo.vai=self.falalogo.vai
        
        self.neide=Elemento(img=NEIDE, style=dict(left=100, top=350, width=300, height="200px"))
        self. neide.entra(todos.leste)
        self.falaneide= Texto(todos.leste, "Seja bem vindo! Esse é o Colégio _______ e estamos contentes em recebe-lo, espero que se adapte a sua nova vida acadêmica.")
        self. neide.vai=self.falaneide.vai
        
        self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        self.menino.entra (todos.leste)
        self.falamenino= Texto(todos.leste, "Muito obrigado, Senhora Neide")
        self.menino.vai=self.falamenino.vai
        
        
        self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        self.menino.entra(todos.sul)
        self.todos.norte.vai()
        
        
        
        self.a=Elemento(img=A, style=dict(left=100, top=350, width=300, height="200px"),vai=self.errou)
        self.b=Elemento(img=B, style=dict (left=300, top=350, width=300, height="200px",),vai=self.acertou)
        self.c=Elemento(img=C,  style=dict(left=600, top=350, width=300, height="200px"),vai=self.errou)
        self.a.entra(todos.sul)
        self.b.entra(todos.sul)
        self.c.entra(todos.sul)
        self.a.vai()
        
    def acertou(self,ev=0):
        self.todos.oeste.vai()
    def errou(self,ev=0):
        self.todos.norte.vai()
       
        
    # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
    #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
    #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
    # mensagens.vai()
    #[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
