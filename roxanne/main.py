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
SALA4= "https://i.imgur.com/Sh5AGVz.jpg"
PERSONAGEM = None
ALAN = "https://i.imgur.com/bO9jojz.png"
GABI = "https://i.imgur.com/MUrxyGb.png"
CARLO = "https://i.imgur.com/94lhgKo.png"
TASSIA = "https://i.imgur.com/Q5PcxvC.png"
LETICIA = "https://i.imgur.com/Oo1sn9s.png"
    

class doidera():
    def __init__(self):
        #laboratorio= Cena(img=LABORATORIO)
        pass
        a=Cenas(congresso)
        congresso.norte.vai=a.vai
        d=Personagens(congresso)
        congresso.norte.vai=d.vai
        c=mendel(congress0)
        congresso.oeste.vai=c.vai
        b=mutassaum(congresso)
        congresso.sul.vai=b.vai
        
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

class mendel():
    def __init__(self):
        self.foi,congresso.oeste.vai=congresso.SALA3.vai,self.vai
        self.congresso=congresso
    
        self.c=Elemento(img= "https://i.imgur.com/MUrxyGb.png", tit="Oiiii, meu nome é Gabi", 
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.acertou)
        
        self.b=Elemento(img= "https://i.imgur.com/Q5PcxvC.png", tit= "Aqui é a Tássia e vamos agilizando porque eu não tenho tempo,pois o tempo é evolução e eu preciso me modificar para me adaptar" ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/bO9jojz.png", tit = "Coé lek. Meu nome é Alan e eu sei que se eu tenho várias tatuagens meus futuros filhos nasceram tatuados",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(congresso.oeste)
        self.b.entra(congresso.oeste)
        self.c.entra(congresso.oeste)
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.congresso.oeste, "A lei de Mendel é uma das leis mais antigas e clássica que existe sobre genética e seus princípios  estão relacionados à transmissão hereditária das características de um organismo a seus filhos ").vai()
        
    def acertou(self,ev=0):
            self.congresso.oeste.vai()
            
    def errou(self,ev=0):
            self.congresso.oeste.vai()
            
            
class mutassaum():
    def __init__(self):
        self.foi,congresso.sul.vai=congresso.SALA4.vai,self.vai
        self.congresso=congresso
    
        self.c=Elemento(img= "https://i.imgur.com/MUrxyGb.png", tit="Oiiii, meu nome é Gabi", 
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.acertou)
        
        self.b=Elemento(img=B, tit= "Dani aqui, pessoaaalll! Vocês acreditam que a professora hoje me obrigou a fazer aquele esporte nojento???? Futebol, eca! É coisa de menino. Fora que eu comprei um short lindissmo rosa e adivinham??? Não combinou com esse uniforme." ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/bO9jojz.png", tit = "Coé lek. Meu nome é Alan e eu sei que se eu tenho várias tatuagens meus futuros filhos nasceram tatuados",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(congresso.sul)
        self.b.entra(congresso.sul)
        self.c.entra(congresso.sul)
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.congresso.sul," Mutação ").vai()
        
    def acertou(self,ev=0):
            self.congresso.sul.vai()
            
    def errou(self,ev=0):
            self.congresso.sul.vai()

    
    

