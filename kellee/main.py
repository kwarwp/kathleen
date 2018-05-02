# kathleen.kellee.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900

FOGO = "http://proec.ufabc.edu.br/quimicaresponde/wp-content/uploads/2015/02/papel-de-parede-fogo-fire-wallpapers-15-e1424831208400.jpg"
AGUA = "http://luizalavenere.blog.uol.com.br/images/water.jpg"
AREIA = "https://upload.wikimedia.org/wikipedia/commons/5/53/Dunas_de_areia.jpg"
HUMANO = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Homo_sapiens.JPG/450px-Homo_sapiens.JPG"

def criarEstoria():
    fogo = Cena(img=FOGO)
    agua = Cena(img=AGUA)
    fogo.direita = agua
    humano = Elemento(img=HUMANO, tit="humano",style = dict(left=400, width=400, hight=400, bottom=400, top=50))
    humano.entra(fogo)
    ehumano=Texto(fogo,"quero agua")
    humano.vai = ehumano.vai
    areia = Cena(img=AREIA)
    agua.direita= areia
    fogo.vai()
    
criarEstoria()