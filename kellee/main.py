
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
#from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
#inicio
SALA1 = "https://i.imgur.com/5cKwnkv.jpg"
#fachada da escola CENA 1
SALA2 = "https://i.imgur.com/5cKwnkv.jpg"
#Sala de aula CENA 2
SALA3 = "https://i.imgur.com/tiJmoBA.jpeg"
#Corredor da escola CENA 4
SALA4 = "https://i.imgur.com/FBbMoQM.jpg"
#Quadra de esportes
SALA5 = "https://i.imgur.com/B2CtFTa.jpg"
#desconhecida 
SALA6 = "https://s3-sa-east-1.amazonaws.com/uploads-ntro/blog/wp-content/uploads/2017/04/06121758/sonhar-com-mar.jpg"
#MENINO= "https://cdn.pixabay.com/photo/2017/07/07/03/21/child-2480290_960_720.png"
PLAY= "https://i.imgur.com/G9QfpN5.png"
#diretora neide RASCUNHO
NEIDE=" https://i.imgur.com/ATlnIzM.png"
PACIENTE="https://i.imgur.com/mcBVqNT.png"
A= "https://i.imgur.com/ADYjJ5F.png"
B= "https://i.imgur.com/x9jVvbX.png"
C= "https://i.imgur.com/74k0IOK.png"
SETINHA= "https://media.giphy.com/media/hqfzJ6el5q5GoHoYO4/giphy.gif"
SETAD ="https://i.imgur.com/DtFfAjo.gif"
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
        
        #self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        #self.menino.entra (todos.leste)
        #self.falamenino= Texto(todos.leste, "Muito obrigado, Senhora Neide")
        #self.menino.vai=self.falamenino.vai
    
        
        self.a=Elemento(img=A,tit= "Balão de fundo redondo",
        style=dict(left=50, top=300, width=400, height="200px"),vai=self.errou)
        
        self.b=Elemento(img=B, tit= "Becker" ,
        style=dict (left=300, top=300, width=300, height="200px",),vai=self.acertou)
        
        self.c=Elemento(img= "https://i.imgur.com/uqUIEXJ.png", tit= "Placa de Petri", 
        style=dict(left=600, top=300, width=200, height="200px"),vai=self.errou)
        
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
        #self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        # self.menino.entra(todas.sul)
        self.c=Elemento(img= "https://i.imgur.com/lQDHDC4.png", tit="Oiiii, meu nome é Toni. Eu tenho 13 anos e estou tão triste. Meus amigos tem me chamado de coisas horriveis e isso me deixa triste. - O trabalho foi baseado nos números da Pesquisa Nacional de Saúde do Escolar (PeNSE) de 2012, que entrevistou 110 mil alunos, representando um universo de mais de três milhões de crianças. O estudo traçou o perfil antropométrico dos estudantes a partir da percepção deles sobre o próprio corpo, numa escala de características como âÂÂmuito magroâÂÂ, âÂÂmagroâÂÂ, âÂÂnormalâÂÂ, âÂÂgordoâÂÂ e âÂÂmuito gordoâÂÂ. Após comparar as respostas das entrevistas, a pesquisa chegou à conclusão que os estereótipos âÂÂmuito magroâÂÂ, âÂÂgordoâÂÂ e âÂÂmuito gordoâÂÂ são os alvos preferidos de perseguições: 11,3%, 12,1% e 23,7% das crianças inseridas nestas categorias, respectivamente, responderam sofrer bullying com frequência- 'https://oglobo.globo.com/sociedade/educacao/alunos-acima-do-peso-sao-mais-vitimas-de-bullying-na-escola-12375170'",   
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.acertou)
        
        self.b=Elemento(img=B, tit= "Dani aqui, pessoaaalll! Vocês acreditam que a professora hoje me obrigou a fazer aquele esporte nojento???? Futebol, eca! É coisa de menino. Fora que eu comprei um short lindissmo rosa e adivinham??? Não combinou com esse uniforme." ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/KaEaDQk.png", tit = "Fala aêê. Meu nome é Rodrigo e hoje eu estou suavee na nave. Dia de futebooool e de zoar o Toni. AQUELE BALEIA DE ÓCULOS ALI KKKKKKK",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(todas.sul)
        self.b.entra(todas.sul)
        self.c.entra(todas.sul)
        #self.a.vai()
        
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.todas.sul,"O becker de vidro é um recipiente cilíndrico utilizado para armazenar, misturar e aquecer líquidos em laboratórios. Muito bem! ").vai()
        
    def acertou(self,ev=0):
            self.todas.oeste.vai()
            
    def errou(self,ev=0):
            self.todas.leste.vai()
        

class cansada():
    def __init__(self,todos):
        self.foi,todos.leste.vai=todos.leste.vai,self.vai
        self.todos=todos
        #self.neide=Elemento(img=NEIDE, style=dict(left=100, top=350, width=300, height="200px"))
        #self.neide.entra(todos.leste)
        
        self.setinha=Elemento(img= SETINHA, tit = "Voltar para início")
        self.setinha.entra(todos.leste)
        self.setinha.vai=self.todos.norte.vai
        
        self.setad=Elemento(img=SETAD, tit= "Proxima cena", 
        style=dict(left=1090, top=350, width=80, height="100px"))
        self.setad.entra(todos.leste)
        self.setad.vai=self.todos.sul.vai
        
        self.bola=Elemento(img = "https://4.bp.blogspot.com/-5tI9f8dEANo/WFJvsXn1pvI/AAAAAAAAX2I/Cbx902UhDIM_cOm-p3JHfKKtTnEJ6QKvgCLcB/s320/Gifs%2Banimados%2BBola%2Bde%2BFutebol%2Bakigifs%2B14.gif",
        style=dict(left=1070, top=350, width=80, height="100px"))
        self.bola.entra(todos.sul)
        self.bola.vai
    
    def vai(self,ev=0):
        self.foi()
        Texto(self.todos.leste,"Para provar ao paciente sobre o uso do remédio em jejum podemos fazer um experimento. Eles são uma maneira prática de aprender e testar seus conhecimentos. Quando um medicamento é ingerido, ele vai para o estômago e parte de seu princípio ativo já é absorvida, entrando na corrente sanguínea. Para demonstrar ao paciente que o medicamento Omeprazol é melhor absorvido em jejum, devemos realizar um experimento simulando a composição existente no estômago.").vai()
        
        
        
class  blabla():
     def __init__(self,todos):
        self.foi,todos.sul.vai=todos.sul.vai,self.vai
        self.todos=todos
        #self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        #self.menino.entra(todos.sul)
    
     def vai(self,ev=0):
        self.foi()
        Texto(self.todos.sul,"Qual das vidrarias você acha que seria ideal?").vai()
        
        
class ajuda():
    def __init__(self,todos):
        self.foi,todos.norte.vai=todos.norte.vai,self.vai
        self.todos=todos
        self.dra= Elemento ( img=NEIDE, tit="Para o alívio dos sintomas você vai precisar tomar um omeprazol ao acordar em jejum.", style=dict(left=100, top=300, width=300, height="200px"))
        self.dra.entra(todos.norte)
        self.paciente= Elemento ( img= PACIENTE, tit="Por que em jejum, dra?", style=dict(left=870, top=60, width=300, height="500px"))
        self.paciente.entra(todos.norte)
        
        self.play = Elemento(img=PLAY, tit="Jogar", style=dict(left=370, top=300, width=300, height="200px"))
        self.play.entra(todos.norte)
        self.play.vai=self.todos.norte.vai
         # self.play = Elemento (img = "ÂÂÂÂÂÂ https://i.imgur.com/G9QfpN5.png", tit="Jogar",
        #style=dict(left=220, top=400, width=120, heigth=120))
        self.play.vai=self.todos.sul.vai
        
    def vai(self,ev=0):
        self.foi()
        #Texto(self.todos.norte, "O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbaridade, e saber o limite de brincadeira e agressão. ").vai()
        self.dr.entra
    
    
        
    # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
    #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
    #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
    # mensagens.vai()
    #[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
