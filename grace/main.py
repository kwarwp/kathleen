from _spy.vittollino.main import Cena,Elemento,Labirinto
from _spy.vittollyno.main import Iventaeio as inv 
ESPACO =" https://img2.gratispng.com/20180630/lyt/kisspng-atmosphere-desktop-wallpaper-space-computer-univer-consciousness-5b374ccd919912.1150048715303507975964.jpg"
PIRANHA = "https://banner2.kisspng.com/20180529/obw/kisspng-piranha-clip-art-5b0da663c055d5.8855324515276212197878.jpg"
class BFF():
    #def__int__(self) 
      espaco=Cena(img=ESPACO)
      piranha=Elemento(img=PIRANHA)
      piranha.entra(espaco)
      espaco.vai()
BFF()