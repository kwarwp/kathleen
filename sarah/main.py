# kathleen.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
#from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
INICIO1 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO2 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO3 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO4 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO5 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO6 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO7 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO8 = "https://i.imgur.com/vFALZ8K.jpg"
INICIO9 = "https://i.imgur.com/vFALZ8K.jpg"
class terror():
	def __init__(self):
    
        self.joao = joao = Sala(n= INICIO1, l= INICIO2, s= INICIO3, o= INICIO4)                      
        self.maria=maria= Sala(o= INICIO5, s= INICIO6, l= INICIO7, n= INICIO8)
        d=hey(naria)
        maria.sul.vai=d.vai
        b=blabla(joao)
        joao.sul.vai=b.vai
        a=cansada(joao)
        todos.leste.vai=a.vai
        c=ajuda(joao)
        todos.norte.vai=c.vai
        self.joao.oeste.vai=self.maria.sul.vai
        self.maria.leste.vai=self.joao.norte.vai
        
        self.a.entra(todos.sul)
        self.b.entra(todos.sul)
        self.c.entra(todos.sul)
        self.a.vai()
        
    def acertou(self,ev=0):
        self.joao.oeste.vai()
    def errou(self,ev=0):
        self.joao.norte.vai()
    npc=Elemento(img="https://i.imgur.com/GbnwrWN.png", style=dict(left=370, top=300, width=300, height="200px")) 
    inicio=Cena(img=INICIO)
    npc.entra(inicio)
    Texto(inicio, "NPC: Acabamos de receber uma mensagem da NASA informando que um dos satélites no espaço detectou um objeto no interior de um núcleo de gelo na região antártica").vai()
    
    inicio.vai()
      def acertou(self,ev=0):
        self.todos.oeste.vai()
    def errou(self,ev=0):
        self.todos.norte.vai()
        
class hey():
    def __init__(self,maria):
        self.foi,maria.sul.vai=maria.sul.vai,self.vai
        self.maria=maria
        #self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        # self.menino.entra(todas.sul)
        self.c=Elemento(img= "https://i.imgur.com/lQDHDC4.png", tit="Oiiii, meu nome é Toni. Eu tenho 13 anos e estou tão triste. Meus amigos tem me chamado de coisas horriveis e isso me deixa triste. - O trabalho foi baseado nos números da Pesquisa Nacional de Saúde do Escolar (PeNSE) de 2012, que entrevistou 110 mil alunos, representando um universo de mais de três milhões de crianças. O estudo traçou o perfil antropométrico dos estudantes a partir da percepção deles sobre o próprio corpo, numa escala de características como âÂÂmuito magroâÂÂ, âÂÂmagroâÂÂ, âÂÂnormalâÂÂ, âÂÂgordoâÂÂ e âÂÂmuito gordoâÂÂ. Após comparar as respostas das entrevistas, a pesquisa chegou à conclusão que os estereótipos âÂÂmuito magroâÂÂ, âÂÂgordoâÂÂ e âÂÂmuito gordoâÂÂ são os alvos preferidos de perseguições: 11,3%, 12,1% e 23,7% das crianças inseridas nestas categorias, respectivamente, responderam sofrer bullying com frequência- 'https://oglobo.globo.com/sociedade/educacao/alunos-acima-do-peso-sao-mais-vitimas-de-bullying-na-escola-12375170'",   
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.acertou)
        
        self.b=Elemento(img= "https://i.imgur.com/KwIY4yn.png", tit= "Dani aqui, pessoaaalll! Vocês acreditam que a professora hoje me obrigou a fazer aquele esporte nojento???? Futebol, eca! É coisa de menino. Fora que eu comprei um short lindissmo rosa e adivinham??? Não combinou com esse uniforme." ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/KaEaDQk.png", tit = "Fala aêê. Meu nome é Rodrigo e hoje eu estou suavee na nave. Dia de futebooool e de zoar o Toni. AQUELE BALEIA DE ÓCULOS ALI KKKKKKK",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(maria.sul)
        self.b.entra(maria.sul)
        self.c.entra(maria.sul)
        #self.a.vai()
        
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.maria.sul,"Parabéns. 'O preconceito da raça é injusto e causa grande sofrimento às pessoas.-Voltaire' Assim como qualquer outro tipo de preconceito!!!!  Agora nossos alunos estão na aula de educação fisíca e você terá que descobrir quem infelizmente tem sofrido Bullying, não apenas nessa aula. ").vai()
        
    def acertou(self,ev=0):
            self.maria.oeste.vai()
            
    def errou(self,ev=0):
            self.maria.leste.vai()
        

class cansada():
    def __init__(self,joao):
        self.foi,joao.leste.vai=joao.leste.vai,self.vai
        self.joao=joao
        self.neide=Elemento(img=NEIDE, style=dict(left=100, top=350, width=300, height="200px"))
        self.neide.entra(joao.leste)
        
        self.setinha=Elemento(img= SETINHA, tit = "Voltar para início")
        self.setinha.entra(joao.leste)
        self.setinha.vai=self.todos.norte.vai
        
        self.setad=Elemento(img=SETAD, tit= "Proxima cena", 
        style=dict(left=1090, top=350, width=80, height="100px"))
        self.setad.entra(joao.leste)
        self.setad.vai=self.joao.sul.vai
        
        self.bola=Elemento(img = "https://4.bp.blogspot.com/-5tI9f8dEANo/WFJvsXn1pvI/AAAAAAAAX2I/Cbx902UhDIM_cOm-p3JHfKKtTnEJ6QKvgCLcB/s320/Gifs%2Banimados%2BBola%2Bde%2BFutebol%2Bakigifs%2B14.gif",
        style=dict(left=1070, top=350, width=80, height="100px"))
        self.bola.entra(joao.sul)
        self.bola.vai
    
    def vai(self,ev=0):
        self.foi()
        Texto(self.joao.leste,"Seja bem vindo! Esse é o Colégio _______ e estamos contentes em recebe-lo, espero que se adapte a sua nova vida acadêmica. Se você estiver pronto aperte na setinha a sua direita").vai()
        
        
        
class  blabla():
     def __init__(self,joao):
        self.foi,joao.sul.vai=joao.sul.vai,self.vai
        self.joao=joao
        #self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        #self.menino.entra(todos.sul)
    
     def vai(self,ev=0):
        self.foi()
        Texto(self.joao.sul,"Esse aqui é o nosso laboratório de ciência. E você terá que fazer uma escolha: Qual deles sofre bullying ? Cada aluno está contando sua história. Passe o mouse em cima de cada um e conheça mais sobre o dia a dia deles.").vai()
        
        
class ajuda():
    def __init__(self,joao):
        self.foi,joao.norte.vai=joao.norte.vai,self.vai
        self.joao=joao
        self.play = Elemento(img=PLAY, tit="Jogar", style=dict(left=370, top=300, width=300, height="200px"))
        self.play.entra(joao.norte)
        self.play.vai=self.joao.norte.vai
         # self.play = Elemento (img = "ÂÂÂÂÂÂ https://i.imgur.com/G9QfpN5.png", tit="Jogar",
        #style=dict(left=220, top=400, width=120, heigth=120))
        self.play.vai=self.joao.leste.vai
        
    def vai(self,ev=0):
        self.foi()
        Texto(self.joao.norte, "O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbaridade, e saber o limite de brincadeira e agressão. ").vai()
        
    
    
        
    # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
    #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
    #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
    # mensagens.vai()
    #[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
     

terror()
