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
#MENINO= "https://cdn.pixabay.com/photo/2017/07/07/03/21/child-2480290_960_720.png"
PLAY= "https://i.imgur.com/G9QfpN5.png"
#diretora neide RASCUNHO
NEIDE=" https://i.imgur.com/ATlnIzM.png"
A= "https://i.imgur.com/frA6jk8.png"
B= " https://i.imgur.com/KwIY4yn.png"
C= "https://i.imgur.com/Brb4yHm.jpg"
SETINHA= "https://media.giphy.com/media/hqfzJ6el5q5GoHoYO4/giphy.gif"
SETAD ="https://www.imagensanimadas.com/data/media/111/seta-imagem-animada-0540.gif"
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
    
        
        self.a=Elemento(img=A, tit= "Olá, eu sou Rosa. Tenho 13 anos. Preciso contar algo terrível que aconteceu. A maquiagem que eu tanto queria acabou no shopping da cidade e nunca que eu irei me submeter a ir na lojinha do interior. Minha vida é uma merda!!!", 
        style=dict(left=50, top=300, width=400, height="200px"),vai=self.errou)
        
        self.b=Elemento(img=B, tit= "Olá, eu sou a Dani. Tenho 14 anos. Estou aqui para te contar sobre algo que infelizmente me doi muito. O preconceito e a discriminação muitas vezes resultam em situações em que pessoas são humilhadas, agredidas e acusadas injustamente simplesmente pelo fato de fazerem parte de algum grupo social específico. A afirmação é de uma pesquisa da Fundação Instituto de Pesquisa Econômicas (Fipe) que publicou em junho, em parceria com o Inep, um estudo sobre preconceito e discriminação no ambiente escolar. De acordo com a pesquisa, as práticas discriminatórias têm como principais vítimas os alunos, especialmente negros, pobres e homossexuais, com médias de 19%, 18% e 17% respectivamente para o índice percentual de conhecimento de situações de bullying nas escolas. - Observatório da Educação. 'http://www.observatoriodaeducacao.org.br/index.php/entrevistas/56-entrevistas/817-criancas-negras-estao-entre-as-principais-vitimas-de-bullying'" ,
        style=dict (left=300, top=300, width=300, height="200px",),vai=self.acertou)
        
        self.c=Elemento(img= "https://i.imgur.com/yuFIURj.png", tit= "Olá, eu sou Pablo. Tenho 15 anos e hoje aconteceu uma tragédia. Meu pai não depositou o valor todo da minha mesada. Não consegui comprar o relógio que eu tanto queria. Aff, pai tóxico", 
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
        self.c=Elemento(img= "https://i.imgur.com/lQDHDC4.png", tit="Oiiii, meu nome é Toni. Eu tenho 13 anos e estou tão triste. Meus amigos tem me chamado de coisas horriveis e isso me deixa triste. - O trabalho foi baseado nos números da Pesquisa Nacional de Saúde do Escolar (PeNSE) de 2012, que entrevistou 110 mil alunos, representando um universo de mais de três milhões de crianças. O estudo traçou o perfil antropométrico dos estudantes a partir da percepção deles sobre o próprio corpo, numa escala de características como âmuito magroâ, âmagroâ, ânormalâ, âgordoâ e âmuito gordoâ. Após comparar as respostas das entrevistas, a pesquisa chegou à conclusão que os estereótipos âmuito magroâ, âgordoâ e âmuito gordoâ são os alvos preferidos de perseguições: 11,3%, 12,1% e 23,7% das crianças inseridas nestas categorias, respectivamente, responderam sofrer bullying com frequência- 'https://oglobo.globo.com/sociedade/educacao/alunos-acima-do-peso-sao-mais-vitimas-de-bullying-na-escola-12375170'",   
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
            Texto(self.todas.sul,"Parabéns. 'O preconceito da raça é injusto e causa grande sofrimento às pessoas.-Voltaire' Assim como qualquer outro tipo de preconceito!!!!  Agora nossos alunos estão na aula de educação fisíca e você terá que descobrir quem infelizmente tem sofrido Bullying, não apenas nessa aula. ").vai()
        
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
        
        self.setinha=Elemento(img= SETINHA, tit = "Voltar para início")
        self.setinha.entra(todos.leste)
        self.setinha.vai=self.todos.norte.vai
        
        self.setad=Elemento(img=SETAD, tit= "Proxima cena", 
        style=dict(left=1090, top=350, width=80, height="100px"))
        self.setad.entra(todos.leste)
        self.setad.vai=self.todos.sul.vai
        
        self.bola=Elemento(img = "https://4.bp.blogspot.com/-5tI9f8dEANo/WFJvsXn1pvI/AAAAAAAAX2I/Cbx902UhDIM_cOm-p3JHfKKtTnEJ6QKvgCLcB/s320/Gifs%2Banimados%2BBola%2Bde%2BFutebol%2Bakigifs%2B14.gif",
        style=dict(left=1070, top=350, width=80, height="100px"))
        self.bola.entra(todas.sul)
        self.bola.vai
    
    def vai(self,ev=0):
        self.foi()
        Texto(self.todos.leste,"Seja bem vindo! Esse é o Colégio _______ e estamos contentes em recebe-lo, espero que se adapte a sua nova vida acadêmica. Se você estiver pronto aperte na setinha a sua direita").vai()
        
        
        
class  blabla():
     def __init__(self,todos):
        self.foi,todos.sul.vai=todos.sul.vai,self.vai
        self.todos=todos
        #self.menino = Elemento(img=MENINO, style=dict(left=600, top=350, width=300, height="200px"))
        #self.menino.entra(todos.sul)
    
     def vai(self,ev=0):
        self.foi()
        Texto(self.todos.sul,"Esse aqui é o nosso laboratório de ciência. E você terá que fazer uma escolha: Qual deles sofre bullying ? Cada aluno está contando sua história. Passe o mouse em cima de cada um e conheça mais sobre o dia a dia deles.").vai()
        
        
class ajuda():
    def __init__(self,todos):
        self.foi,todos.norte.vai=todos.norte.vai,self.vai
        self.todos=todos
        self.play = Elemento(img=PLAY, tit="Jogar", style=dict(left=370, top=300, width=300, height="200px"))
        self.play.entra(todos.norte)
        self.play.vai=self.todos.norte.vai
         # self.play = Elemento (img = "ÂÂÂÂÂ https://i.imgur.com/G9QfpN5.png", tit="Jogar",
        #style=dict(left=220, top=400, width=120, heigth=120))
        self.play.vai=self.todos.leste.vai
        
    def vai(self,ev=0):
        self.foi()
        Texto(self.todos.norte, "O intuito do jogo é fazer com que as pessoas tenham ciência de que a prática do bullying pode causar mal à saúde humana. Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbaridade, e saber o limite de brincadeira e agressão. ").vai()
        
    
    
        
    # mensagens= Codigo(cena=todos.norte, topo="", codigo="O intuito do jogo é fazer com que as pessoas", 
    #"tenham ciência de que a , prática do bullying pode causar mal à saúde humana."),
    #"Resultando em aspectos que possam dificultar o cotidiano de quem é alvo dessa barbárie, e, saber o limite de brincadeira e agressão.") 
    # mensagens.vai()
    #[ sala1, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  
                 
                  
        
OI()
