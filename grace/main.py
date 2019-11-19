# kathleen.grace.main.py
from _spy.vitollino.main import Cena,Elemento,Labirinto e Texto
from _spy.vitollino.main import INVENTARIO as inv
#STYLE=["width"] = 800
#STYLE=["height"] = "600px"


CHARLES="https://thumbs.dreamstime.com/b/homem-novo-fan%C3%A1tico-estilo-da-rua-do-menino-da-intimida%C3%A7%C3%A3o-no-branco-png-dispon%C3%ADvel-68251163.jpg"
LABORATORIO=""
LABOTY=""
AJUDANTE=""
POLICIA=""
LIVRO=""
FOLHA=""
PRACA=""
TECLADO=""
class bruninha ():
    laboratorio=Cena(img=LABORATORIO)
    livro=Cena(img=LIVRO)
    laboty=Cena(img=LABOTY)
    charles=Elemento(img=CHARLES)
    folha=Elemento(img=FOLHA)
    praca=Cena(img=PRACA)
    laboratorio.direita=laboty
    laboty.direita=livro
    livro.direita=praca
    praca.esquerda=livro
    livro.esquerda=laboty
    laboty.esquerda=laboratorio
    charles=Elemento(img=CHARLES)
    ajudante=Elemento(img=AJUDANTE)
    policia=Elemento(img=POLICIA)
    teclado=Elemento(img=TECLADO)
    folha=Elemento(img=FOLHA)
    charles.entra(laboratorio)
    
    charles=Texto(labotorio, "O que aconteceu aqui? Onde está o meu antídoto?")
    charles.vai=falacharles.vai
    
    ajudante.entra(laboty)
    
    ajudante=Texto(laboty, "invadiram a casa do Neytan e o levaram.Por favor chame ajuda!")
    ajudante.vai=falaajudante.vai
    
    charles.entra(livro)
    policia.entra(laboratorio)
    
    policia=Texto(laboratorio, "NÂO MEXE EM NADA! RALA MERMÂO!")
    folha.entra(praca)
    
    folha=Texto(praca, " UUU (Phe/F) FenilalaninaU(Phe/F) FenilalaninaUC")
    
    
 
    
    
    
    
    
    
    
bruninha()