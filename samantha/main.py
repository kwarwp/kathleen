# kathleen.samantha.main.py
from_spy.vitollino.main import Cena, Elemento, Labirinto

from_spy.vitollino.main import INVENTARIO as inv 

ANA_MARIA= "http://classroomclipart.com/clipart-view/Clipart/Science/girl-science-student-wearing-a-lab-coat-and-goggles-clipart_jpg.htm"

DR_ZUCKMAN= "https://cdn3.vectorstock.com/i/1000x1000/51/82/scientist-man-handsome-cartoon-character-vector-22385182.jpg"

COFRE1= "https://eletronicasantana.vteximg.com.br/arquivos/ids/60948-1000-1000/cofre-eletronico-15ef-safewell.jpg?v=636742448074400000"

//sala dos computadores

SALA1= "http://www.ocf.berkeley.edu/~edy/computerroom.jpg"

//tela PC do computador com senha

SALA2= "imagem.jpg"

//cena PC depois de desbloqueado

SALA3= "imagem.jpg"

//sala do cofre

SALA4= "imagem.jpg"

//cofre cena

SALA5= "imagem.jpg"

//dentro do cofre

SALA6= "imagem.jpg"

Class Zeus ():

def _ int _ (self)

ana_maria= Elemento (img=ANA_MARIA)

dr_zuckman= Elemento (img=DR_ZUCKMAN)

laboratorio= Cena (img=LABORATORIO)

cofre1= Cena (img=COFRE1)

cofre2= Elemnto (img=ELEMENTO, Tit= "COFRE", (STYLE=600, top=60, left= 100, width= 90))

lugar=labirinto (n=SALA1, l=SALA2, o=SALA3, s=SALA4)

lugar2=labirinto (s=SALA4, l=SALA5, o=SALA6, n=SALA1)

//ordem das cenas: sala1, sala2, sala3, sala4, sala5,sala6,sala4,sala1)

ana_maria.entra(lugar.norte)

dr_zuckman.entra(lugar.norte)

//a ana maria entra no computador para escrever a senha (cena 2)

ana_maria.entra(lugar.leste)

//a ana maria depois que acertar a cena entra na pasta do pc em que vários codons embaralhados, na tela mesmo, ela vai desembaralhar e o resultado é a senha do cofre

ana_maria.entra(lugar.oeste)

//ana maria entra na sala dos cofres

ana.maria.entra(lugar.sul)

lugar.norte.vai( 