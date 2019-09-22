# kathleen.morgan.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto
from _spy.vitollino.main import Inventario as inv


GABINETE = 
DELEGACIA = 
FESTA = 
CEMITERIO =
DELEGADO =
MORDOMO =
POLITICO = 
HOMEM =
PASSISTA =


class TORDO():
      #def __ int __(self):
        festa = Cena ( img = FESTA  )
        gabinete = Cena ( img = GABINETE )
        delegacia = Cena ( img = DELEGACIA )
        cemiterio = Cena ( img = CEMITERIO )
        delegado = Elemento ( img = DELEGADO )
        mordomo = Elemento ( img = MORDOMO )
        politico = Elemento ( img = POLITICO )
        homem = Elemento ( img = HOMEM )
        passista = Elemento ( img = PASSISTA )
        lugar = Labirinto (n= GABINETE, l= FESTA, o= DELEGACIA, s= CEMITERIO)
        
        delegado.entra(lugar.norte)
        mordomo.entra(lugar.norte)
        politico.entra(lugar.norte)
        lugar.norte.vai()
        
        passista.entra(lugar.leste)
        mordomo.entra(lugar.leste)
        homem.entra(lugar.leste)
        lugar.leste.vai()
        
        homem.entra(lugar.oeste)
        lugar.oeste.vai()
        
        homem.entra(lugar.sul)
        mordomo.entra(lugar.sul)
        politico.entra(lugar.sul)
        delegado.entra(lugar.sul)
        lugar.sul.vai()
        
        TORDO():
        
        
