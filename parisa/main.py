# kathleen.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
#inicio
SALA1 = "https://i.imgur.com/RGO9pjB.jpg"
#fachada da escola CENA 1
SALA2 = "https://i.imgur.com/klmWAtd.png"
#Sala de aula CENA 2
SALA3 = "https://i.imgur.com/51la4f1.jpg"
#Corredor da escola CENA 4
SALA4 = "https://i.imgur.com/0xs8URf.jpg"
#Quadra de esportes
SALA5 = "https://i.pinimg.com/originals/78/99/c9/7899c925ee95618ef0bd21f4b067175b.jpg"
#desconhecida 
SALA6 = "https://s3-sa-east-1.amazonaws.com/uploads-ntro/blog/wp-content/uploads/2017/04/06121758/sonhar-com-mar.jpg"
MENINO= "https://cdn.pixabay.com/photo/2017/07/07/03/21/child-2480290_960_720.png"
PLAY= "https://i.imgur.com/G9QfpN5.png"
#diretora neide RASCUNHO
NEIDE=" https://i.imgur.com/ATlnIzM.png"
A= "https://i.imgur.com/frA6jk8.png"
B= " https://i.imgur.com/KwIY4yn.png"
C= "https://i.imgur.com/Brb4yHm.jpg"

class OI():
    def __init__(self):
    
    
       
        
    
        self.todos = todos = Sala(n= SALA1, l= SALA2, s= SALA3, o= SALA4)                      
        self.todas=todas= Sala(o= SALA4, s= SALA5, l= SALA6, n= SALA1)
        d=hey(todas)
        todas.sul.vai=d.vai
        b=blabla(todos)
        todos.sul.vai=b.vai
        a=cansada(todos)
        todos.leste.vai=a.vai
        c=ajuda(todos)
        todos.norte.vai=c.vai
        self.todos.oeste.vai=self.todas.sul.vai
        self.todas.leste.vai=self.todos.norte.vai
        #self.todos.norte.vai
        #self.todas.oeste.vai
        
        
      
        self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        self.menino.entra (todos.leste)
        self.falamenino= Texto(todos.leste, "Muito obrigado, Senhora Neide")
        self.menino.vai=self.falamenino.vai
    
        
        self.a=Elemento(img=A, style=dict(left=100, top=100, width=50, height="200px"),vai=self.errou)
        self.b=Elemento(img=B, style=dict (left=300, top=100, width=50, height="200px",),vai=self.acertou)
        self.c=Elemento(img=C,  style=dict(left=600, top=100, width=50, height="200px"),vai=self.errou)
        self.a.entra(todos.sul)
        self.b.entra(todos.sul)
        self.c.entra(todos.sul)
        self.a.vai()
        
    def acertou(self,ev=0):
        self.todos.oeste.vai()
    def errou(self,ev=0):
        self.todos.norte.vai()
        
class hey():
    def __init__(self,todas):
        self.foi,todas.sul.vai=todas.sul.vai,self.vai
        self.todas=todas
        self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        self.menino.entra(todas.sul)
        self.a=Elemento(img=A, style=dict(left=100, top=100, width=50, height="200px"),vai=self.acertou)
        self.b=Elemento(img=B, style=dict (left=300, top=100, width=50, height="200px",),vai=self.errou)
        self.c=Elemento(img=C,  style=dict(left=600, top=100, width=50, height="200px"),vai=self.errou)
        self.a.entra(todas.sul)
        self.b.entra(todas.sul)
        self.c.entra(todas.sul)
        #self.a.vai()
        
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.todas.sul,"uuuuuu").vai()
        
    def acertou(self,ev=0):
            self.todas.oeste.vai()
            
    def errou(self,ev=0):
            self.todas.leste.vai()
        
       
        
   
        
class cansada():
    def __init__(self,todos):
        self.foi,todos.leste.vai=todos.leste.vai,self.vai
        self.todos=todos
        self.neide=Elemento(img=NEIDE, style=dict(left=100, top=350, width=300, height="200px"))
        self.neide.entra(todos.leste)
        
    def vai(self,ev=0):
        self.foi()
        Texto(self.todos.leste,"Seja bem vindo! Esse é o Colégio _______ e estamos contentes em recebe-lo, espero que se adapte a sua nova vida acadêmica.").vai()
        
        
        
class  blabla():
     def __init__(self,todos):
        self.foi,todos.sul.vai=todos.sul.vai,self.vai
        self.todos=todos
        self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        self.menino.entra(todos.sul)
    
     def vai(self,ev=0):
        self.foi()
        Texto(self.todos.sul,"kkkkkkkk").vai()
        
        
class ajuda():
    def __init__(self,todos):
        self.foi,todos.norte.vai=todos.norte.vai,self.vai
        self.todos=todos
        self.play = Elemento(img=PLAY, tit="Jogar", style=dict(left=370, top=300, width=400, height="200px"))
        self.play.entra(todos.norte)
         # self.play = Elemento (img = " https://i.imgur.com/G9QfpN5.png", tit="Jogar",
        #style=dict(left=220, top=400, width=120, heigth=120))
        
        
    def vai(self,ev=0):
        self.foi()
        Texto(self.todos.norte, "O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbaridade, e saber o limite de brincadeira e agressão. ").vai()
        
    
    
                               
       
        
    # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
    #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
    #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
    # mensagens.vai()
    #[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
