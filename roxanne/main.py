# kathleen.roxanne.main.py
from _spy.vitollino.main import Cena, Texto, STYLE,Sala
from _spy.vitollino.main import INVENTARIO as inv
from elemento.main import Elemento 
STYLE["width"] = 800
STYLE["height"] = "600px"


LABORATORIO = "http://lorempixel.com/800/600/city"
PAPEIS = "https://i.imgur.com/qqpUJWF.jpg"
ANA_MARIA = "https://i.imgur.com/qvuwHvs.png"
DR_ZUKMAN = "http://lorempixel.com/800/600/people/2"
PORTA = "https://static.vecteezy.com/system/resources/previews/000/333/044/non_2x/vector-doors-closed-and-open.jpg"
HOSPITAL = "http://lorempixel.com/800/600/city"
COFRE = "http://lorempixel.com/800/600/city"
PAPEIS = "http://lorempixel.com/800/600/city"
SALA1= "https://i.imgur.com/HROYxV1.jpg"
SALA2= "https://i.imgur.com/I5WMU7Y.jpg"
SALA3= "https://i.imgur.com/VCzMJ7t.jpg"
SALA4= "http://lorempixel.com/800/600/city/4"
PERSONAGEM = None
ALAN = "https://i.imgur.com/bO9jojz.png"
GABI = "https://i.imgur.com/MUrxyGb.png"
CARLO = "https://i.imgur.com/94lhgKo.png"
TASSIA = "https://i.imgur.com/Q5PcxvC.png"
LETICIA = "https://i.imgur.com/Oo1sn9s.png
    

class doidera():
    def __init__(self):
        #laboratorio= Cena(img=LABORATORIO)
        pass
class Personagens():
    def __init__(self,imagem = ANA_MARIA, nome ="Ola, eu sou a Ana Paula é um prazer estar com vocês, sou mestra e professorA DE BIOLOGIA e estou aqui para ajudar vocês nos conceitos de genéticas e nas provas que terão, aprendendo de uma maneira divertida"):
        self.ana_maria= Elemento(img=imagem, tit=nome, drag=True, style=dict(
            left=150,top=330,width=300,heigth="250px"))
        #dr_zukman=Elemento(img=DR_ZUKMAN, style=dict(
        #left=200, top=10, width=60, height="60px")) 
    def some(self):
        self.ana_maria.entra(Cena())
    def entra(self,lugar):
        self.ana_maria.entra(lugar)
class Porta(): 
    def __init__(self):
        dragger=dict(Aninha=self.entra_porta)
        self.porta=Elemento(img=PORTA,tit="portela", drop=dragger, style=dict(
         left=170,top=260, width=55,height="150px"))
    def entra (self,lugar):
        self.porta.entra(lugar)
    def entra_porta(self,evento,nome):
        PERSONAGEM.some()
class Cenas():
    def __init__(self): 

        self.congresso= congresso = Sala(n=SALA1,l=SALA2,o= SALA3, s=SALA4)
        PERSONAGEM.entra(congresso.norte)
        # dr_zukman.entra(congresso.norte)
        Porta().entra(congresso.norte)
        congresso.norte.vai()
    def entra_porta(self,evento,nome):
        PERSONAGEM.some()
PERSONAGEM=Personagens()
Cenas()
#doidera()

class eitcha():
    def __init__(self):
    
        self.c=Elemento(img= "https://i.imgur.com/lQDHDC4.png", tit="Oiiii, meu nome é Toni. Eu tenho 13 anos e estou tão triste. Meus amigos tem me chamado de coisas horriveis e isso me deixa triste. - O trabalho foi baseado nos números da Pesquisa Nacional de Saúde do Escolar (PeNSE) de 2012, que entrevistou 110 mil alunos, representando um universo de mais de três milhões de crianças. O estudo traçou o perfil antropométrico dos estudantes a partir da percepção deles sobre o próprio corpo, numa escala de características como âÂÂÂÂÂÂmuito magroâÂÂÂÂÂÂ, âÂÂÂÂÂÂmagroâÂÂÂÂÂÂ, âÂÂÂÂÂÂnormalâÂÂÂÂÂÂ, âÂÂÂÂÂÂgordoâÂÂÂÂÂÂ e âÂÂÂÂÂÂmuito gordoâÂÂÂÂÂÂ. Após comparar as respostas das entrevistas, a pesquisa chegou à conclusão que os estereótipos âÂÂÂÂÂÂmuito magroâÂÂÂÂÂÂ, âÂÂÂÂÂÂgordoâÂÂÂÂÂÂ e âÂÂÂÂÂÂmuito gordoâÂÂÂÂÂÂ são os alvos preferidos de perseguições: 11,3%, 12,1% e 23,7% das crianças inseridas nestas categorias, respectivamente, responderam sofrer bullying com frequência- 'https://oglobo.globo.com/sociedade/educacao/alunos-acima-do-peso-sao-mais-vitimas-de-bullying-na-escola-12375170'",   
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.acertou)
        
        self.b=Elemento(img=B, tit= "Dani aqui, pessoaaalll! Vocês acreditam que a professora hoje me obrigou a fazer aquele esporte nojento???? Futebol, eca! É coisa de menino. Fora que eu comprei um short lindissmo rosa e adivinham??? Não combinou com esse uniforme." ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/KaEaDQk.png", tit = "Fala aêê. Meu nome é Rodrigo e hoje eu estou suavee na nave. Dia de futebooool e de zoar o Toni. AQUELE BALEIA DE ÓCULOS ALI KKKKKKK",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(congresso.oeste)
        self.b.entra(congresso.oeste)
        self.c.entra(congresso.oeste)
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.congresso.oeste, "O preconceito da raça é injusto e causa grande sofrimento às pessoas.-Voltaire' Assim como qualquer outro tipo de preconceito!!!!  Agora nossos alunos estão na aula de educação fisíca e você terá que descobrir quem infelizmente tem sofrido Bullying, não apenas nessa aula. ").vai()
        
    def acertou(self,ev=0):
            self.congresso.oeste.vai()
            
    def errou(self,ev=0):
            self.congresso.oeste.vai()
        

    
    

