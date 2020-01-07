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
SALA2= "http://www.fiocruz.br/ioc/media/insetosdentro_02.jpg"
SALA3= "https://i.imgur.com/VCzMJ7t.jpg"
SALA4= "https://i.imgur.com/Sh5AGVz.jpg"
PERSONAGEM = None
ALAN = "https://i.imgur.com/bO9jojz.png"
GABI = "https://i.imgur.com/MUrxyGb.png"
CARLO = "https://i.imgur.com/94lhgKo.png"
TASSIA = "https://i.imgur.com/Q5PcxvC.png"
LETICIA = "https://i.imgur.com/Oo1sn9s.png"
    

class TakeFioCruz():  #  Nome significativo da classe e use CamelCase, a primeira letra das palavras em maiusculo (PEP8)
    def __init__(self):
        #laboratorio= Cena(img=LABORATORIO)
        pass
        self.congresso= congresso = Sala(n=SALA1,l=SALA2,o= SALA3, s=SALA4)  # monta a sala para o TakeFioCruz
        d=Personagens()  # não usa o (congresso)
        a=Cenas(congresso, d)
        # congresso.norte.vai=a.vai
        c=Mendel(congresso)
        # congresso.oeste.vai=c.vai
        #congresso.norte.vai=d.vai
        #return
        b=Mutassaum(congresso)
        # congresso.sul.vai=b.vai
        e=Borboletas(congresso)
        # congresso.leste.vai=e.vai
        
        #self.congresso.norte.vai=self.congresso.leste.vai
        #self.congresso.oeste.vai=self.congresso.sul.vai
        
class Personagens():
    def __init__(self,imagem = ANA_MARIA, nome ="Ola, eu sou a Ana Paula é um prazer estar com vocês, sou mestra e professorA DE BIOLOGIA e estou aqui para ajudar vocês nos conceitos de genéticas e nas provas que terão, aprendendo de uma maneira divertida"):
        nome= "Aninha" # -XXX- O nome, isto é o tit do elemento tem que ser Aninha porque foi o que usou no dropper
        self.ana_maria= Elemento(img=imagem, tit=nome, drag=True, style=dict(
            left=150,top=330,width=200,heigth="1000px"))
        #dr_zukman=Elemento(img=DR_ZUKMAN, style=dict(
        #left=200, top=10, width=60, height="60px")) 
    def some(self):
        self.ana_maria.entra(Cena())
    def entra(self,lugar):
        self.ana_maria.entra(lugar)

class Porta(): 
    def __init__(self, personagem):  # tem que passar o personagem aqui
        self.personagem = personagem
        dragger=dict(Aninha=self.entra_porta)
        self.porta=Elemento(img=PORTA,tit="portela", drop=dragger, style=dict(
         left=170,top=260, width=55,height="150px"))
    def entra (self,lugar):
        self.porta.entra(lugar)
    def entra_porta(self,evento,nome):
        self.personagem.some()
class Cenas():
    def __init__(self, congresso, personagem):  # tem que passar o congresso e personagem aqui
        self.aqui = aqui = congresso.norte
        self.foi, self.aqui.vai = self.aqui.vai, self.vai
        self.personagem = personagem
        # self.congresso= congresso = Sala(n=SALA1,l=SALA2,o= SALA3, s=SALA4) foi para o TakeFioCruz
        self,personagem.entra(aqui)
        # dr_zukman.entra(congresso.norte)
        Porta(self.personagem).entra(aqui)
        self.vai()
    def entra_porta(self,evento,nome):
        self,personagem.some()
        
    def vai(self,ev=0):
        self.foi()
        nome ="Ola, eu sou a Ana Paula é um prazer estar com vocês, sou mestra e professorA DE BIOLOGIA"\
        "e estou aqui para ajudar vocês nos conceitos de genéticas"\
        "e nas provas que terão, aprendendo de uma maneira divertida"
        Texto(self.aqui, nome).vai()
# PERSONAGEM=Personagens()
# Cenas()
#doidera()

class Mendel():
    def __init__(self, congresso):  # tem que passar o congresso aqui
        # self.foi,congresso.oeste.vai=congresso.SALA3.vai,self.vai
        self.aqui = aqui = congresso.oeste
        self.foi, self.aqui.vai = self.aqui.vai, self.vai
    
        self.c=Elemento(img=GABI, tit="Oiiii, meu nome é Gabi e estou estudando sobre cruzamento de genes e vi que se uma pessoa te AA e outra Aa então seus futuros filhos serão 50% AA e 50% Aa",
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.acertou)
        
        self.b=Elemento(img= "https://i.imgur.com/Q5PcxvC.png", tit= "Aqui é a Tássia e vamos agilizando porque eu não tenho tempo,pois o tempo é evolução e eu preciso me modificar para me adaptar" ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/bO9jojz.png", tit = "Coé lek. Meu nome é Alan e eu sei que se eu tenho várias tatuagens meus futuros filhos nasceram tatuados",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(congresso.oeste)
        self.b.entra(congresso.oeste)
        self.c.entra(congresso.oeste)
        # self.a.vai()
        
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.aqui, "A lei de Mendel é uma das leis mais antigas e clássica que existe sobre genética e seus princípios  estão relacionados à transmissão hereditária das características de um organismo a seus filhos . Agora com seus conhecimento nos ajude a descobrir quem está mais certo").vai()
        
    def acertou(self,ev=0):
            Texto(self.aqui, "Obrigado por me ensinar isso").vai()
            
    def errou(self,ev=0):
            Texto(self.aqui, "Talvez tenhamos que estudar mais", foi=self.vai).vai()
            #self.vai()
            
            
class Mutassaum():
    def __init__(self, congresso):  # tem que passar o congresso aqui
        #self.foi,congresso.sul.vai=congresso.SALA4.vai,self.vai
        self.aqui = aqui = congresso.sul
        self.foi, self.aqui.vai = self.aqui.vai, self.vai
    
        self.c=Elemento(img= "https://i.imgur.com/bO9jojz.png", tit="Como vocês já me conhecem e percebi que quando duas pessoas se conhecem elas começam a se adaptar umas as outras fazendo com que seu DNA mude por transmissão de pensamento", 
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.errou)
        
        self.b=Elemento(img="https://i.imgur.com/94lhgKo.png", tit= "OIe eu sou o Carlo e sei que quando um ser vivo(seres humanos, plantas etc) fica exposto a radiação ou algum produto químico por muito tempo pode ocorre mutação no DNA da pessoa fazendo com que  a pessoa tenha alguma doença ou passe para os seus filho" ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.acertou)

        self.a=Elemento(img= "https://i.imgur.com/Oo1sn9s.png", tit = "OIii sou a Letícia e descobri que quando se come maçã estragada isso pode modificar seu DNA pelas proteínas e enzimas que soltam no seu estômago passam para o sangue e vão até o núcleo das células alterando a sintese de proteínas do corpo",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.errou)

        self.a.entra(congresso.sul)
        self.b.entra(congresso.sul)
        self.c.entra(congresso.sul)
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.aqui," A mutação na enzima tirozinase que transforma o aminoácido tirozina em pigmento da pele, a melanina. Esta doença ocorre em animais e nas plantas e é hereditária. A partir dessa mensagem e do conhecimento que tem ajude a descobrir quem está correto sobre a afirmação ").vai()
        
    def acertou(self,ev=0):
            Texto(self.aqui, "Obrigado por me ensinar isso").vai()
            
    def errou(self,ev=0):
            Texto(self.aqui, "Talvez tenhamos que estudar mais", foi=self.vai).vai()
            #self.vai()
            
            
class Borboletas():
    def __init__(self, congresso):  # tem que passar o congresso aqui
        #self.foi,congresso.sul.vai=congresso.SALA2.vai,self.vai
        self.aqui = aqui = congresso.leste
        self.foi, self.aqui.vai = self.aqui.vai, self.vai
    
        self.c=Elemento(img= "https://i.imgur.com/MUrxyGb.png", tit="Tassia sou eu e digo que as borboletas são adaptadas ao ambiente, quanto mais poluído o ambiente mais cinza", 
        style=dict(left=50, top=350, width=400, height="200px"),vai=self.errou)
        
        self.b=Elemento(img="https://i.imgur.com/Oo1sn9s.png", tit= "As borboletas dos países frios são menos coloridas do que o Brasil pois não pegam sol." ,
        style=dict (left=400, top=350, width=300, height="200px",),vai=self.errou)

        self.a=Elemento(img= "https://i.imgur.com/bO9jojz.png", tit = "descobri que as borboletas podem sofrer mutações sobre alguma dessas fases e não chegar até o ultimo estágio ou morrer antes mesmo de completar a vida adulta",
        style=dict(left=700, top=350, width=400, height="200px"),vai=self.acertou)

        self.a.entra(congresso.leste)
        self.b.entra(congresso.leste)
        self.c.entra(congresso.leste)
        
    def vai(self,ev=0):
            self.foi()
            Texto(self.aqui," As borboletas  são conhecidas por suas cores e por sua vida dividia em 4 estágios:: ovo, larva, pupa e imago (Adulto) e por esse conhecimento prévio diga-nos quais dos estudantes estão corretos ").vai()
        
    def acertou(self,ev=0):
            Texto(self.aqui, "Obrigado por me ensinar isso").vai()
            
    def errou(self,ev=0):
            Texto(self.aqui, "Talvez tenhamos que estudar mais", foi=self.vai).vai()
            #self.vai()

if __name__ == "__main__":
    TakeFioCruz()

