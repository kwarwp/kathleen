# kathleen.anastasia.main.py // HISTÓRIA DO GRUPO DO ALAN

from _spy.vitollino.main import Cena, Elemento, Labirinto 
from _spy.vitollino.main import Inventario as inv 

AVATAR = "img.png"
LAB_DR = "img.png"
PC_LAB = "IMAGEM DO PC QUE DEVERÁ TER AS INFORMAÇÕES DA FASE 2 DA HISTÓRIA"
SALA_COFRE = "img.png"
COFRE_SALA = "img.png"
PC2_SALA = "TODAS AS INFO DA FASE 4"

class GIRIPOCA ():
    #def __ int __ (self):
    avatar = Elemento (img= AVATAR)
    lab_dr = Cena (img= LAB_DR)
    pc_lab = Elemento (img= PC_LAB)
    sala_cofre = Cena (img = SALA_COFRE)
    cofre_sala = Cena (img = COFRE)
    pc2 = Elemento (img = PC2_SALA)
    lugar = Labirinto (n=LAB_DR, l=SALA_COFRE)
    avatar.entra(lugar.norte)
    lugar.norte.vai()
    
    
