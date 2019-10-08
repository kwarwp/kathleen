# kathleen.soraya.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto,  STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"

BRASAO="https://upload.wikimedia.org/wikipedia/commons/9/9a/Fiocruz.jpg"
BIBLIOTECA="https://live.staticflickr.com/30/65319105_09adc58261_z.jpg"
CABECA="https://cdn.pixabay.com/photo/2017/07/13/12/55/puzzle-2500333_960_720.jpg"
JARDIM="https://www.fiocruzimagens.fiocruz.br/image.php?mediaID=MzgxNDc2NGFhNjA0ZTE=&type=sample&folderID=OTQ3NjRhYTYwNGUx&seo="

class Verao ():
    def __init__(self):
        self.BIBLIOTECA=Cena (img= BIBLIOTECA)
        self.BRASAO=Elemento (img= BRASAO, cena=self.BIBLIOTECA, tit = "brasao" ,)
        self.JARDIM=Cena (img= JARDIM, esquerda=self.BIBLIOTECA)
        self.CABECA=Elemento (img= CABECA, cena=self.JARDIM, tit = "cabeca" ,)
        self.BIBLIOTECA.direita=self.JARDIM

    
        self.BIBLIOTECA.vai()
        
if __name__ == "__main__":
    Verao()