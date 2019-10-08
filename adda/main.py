# kathleen.adda.main.py 
from _spy.vittolino.main import  Cena, Elemento, Labirinto, Texto
from _spy.vittolino.main import Inventario as inv
AYDA = "img da ayda"
NPC_KAYLA = "img da npc"
SALA1_LAB = "sala do oswaldin com o computador"
COMPUTADOR_SALA1 = "computador desafio.elemento"
SALA2_COFRE = "sala onde vai estar o cofre"
COFRE_SALA2 = "foto elemento"
class Tordo():
    oswaldin = Elemento(img=)
    ayda = Elemento(img=)
    kayla = Elemento(img=)
    sala1 = Cena(img=)
    computador = Elemento(img=)
    sala2 = Cena(img=)
    cofre = Elemento(img=)
    
    kayla.entra(sala1)
    falakayla = Texto (sala1,"Olá, aqui é Kayla, inteligência criada pelo Dr. Oswaldinho. Ele está desaparecido e tem uma gangue de cientistas loucos querendo roubar sua fórmula recém criada, você preisa encontrar antes deles!")
    ayda.entra(sala1)
    
        