# kathleen.adda.main.py 
from _spy.vittolino.main import  Cena, Elemento, Labirinto, Texto
from _spy.vittolino.main import Inventario as inv

AYDA = "img da ayda"
NPC_KAYLA = "img da npc"
SALA1_LAB = "sala do oswaldin com o computador"
COMPUTADOR_SALA1 = "computador desafio.elemento"
COMPUTADOR_ELE1 = "tela computador"
COMPUTADOR_ELE2 = "tela comp. 2"
SALA2_COFRE = "sala onde vai estar o cofre"
COFRE_SALA2 = "foto elemento"

class Tordo():
    def __init__(self):
        self.oswaldin = Elemento(img=)
        self.ayda = Elemento(img=)
        self.kayla = Elemento(img=)
        self.sala1 = Cena(img=)
        self.computador = Elemento(img=)
        self.compcena = Cena(img=)
        self.sala2 = Cena(img=)
        self.cofre = Elemento(img=)

        self.kayla.entra(sala1)
        self.falakayla = Texto (sala1,"Olá, aqui é Kayla, inteligência criada pelo Dr. Oswaldinho. Ele está desaparecido e tem uma gangue de cientistas loucos querendo roubar sua fórmula recém criada, você preisa encontrar antes deles!")
        self.ayda.entra(sala1)
        self.computador.vai = self.compcena.vai
        MENSAGENS = [
                  [ compcena, "Síntese de proteína ?" "Na síntese de proteína ocorre a tradução do código genético e a formação de proteínas"]
                  ]
                  
        
        
        
    
    
        