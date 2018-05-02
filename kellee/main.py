# kathleen.kellee.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO as inv
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900


class criarsalas():
     def __init__(self):
        self.elementos()     
     def elementos(self):
        FOGO = "http://proec.ufabc.edu.br/quimicaresponde/wp-content/uploads/2015/02/papel-de-parede-fogo-fire-wallpapers-15-e1424831208400.jpg"
        AGUA = "http://luizalavenere.blog.uol.com.br/images/water.jpg"
        AREIA = "https://upload.wikimedia.org/wikipedia/commons/5/53/Dunas_de_areia.jpg"
        HUMANO = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Homo_sapiens.JPG/450px-Homo_sapiens.JPG"

        self.fogo = Cena(img=FOGO)
        self.agua = Cena(img=AGUA)
        self.fogo.direita = self.agua
        self.humano = Elemento(img=HUMANO, tit="humano",style = dict(left=100, width=100, hight=100, bottom=100, top=100))
        self.humano.entra(self.fogo)
        self.ehumano=Texto(self.fogo,"quero agua")
        self.humano.vai= self.ehumano.vai
        self.areia = Cena(img=AREIA)
        self.agua.direita= self.areia
        self.fogo.vai
        
if __name__ == "__main__":
    criarsalas()
    
    
    