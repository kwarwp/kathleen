# kathleen.soraya.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto
from _spy.vitollino.main import INVENTARIO as inv
BRASAO="https://upload.wikimedia.org/wikipedia/commons/9/9a/Fiocruz.jpg"
BIBLIOTECA="https://live.staticflickr.com/30/65319105_09adc58261_z.jpg"
CABECA="https://cdn.pixabay.com/photo/2017/07/13/12/55/puzzle-2500333_960_720.jpg"
JARDIM="https://www.fiocruzimagens.fiocruz.br/image.php?mediaID=MzgxNDc2NGFhNjA0ZTE=&type=sample&folderID=OTQ3NjRhYTYwNGUx&seo="
BIBLIOTECA=Cena (BIBLIOTECA)
BRASAO=Elemento (BRASAO, cena=BIBLIOTECA)
JARDIM=Cena (JARDIM, BIBLIOTECA)
CABECA=Elemento (CABECA, cena=JARDIM)
BIBLIOTECA.direita=JARDIM
class Verao ():
    def __init__(self):
        JARDIM.vai()
        
if __name__ == "__main__":
    Verao()