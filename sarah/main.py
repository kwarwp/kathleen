# kathleen.sarah.main.py
from _spy.vitollino.main import Cena, Elemento
from _spy.vitollino.main import INVENTARIO as inv
PISTA="https://cdn.aquelamaquina.pt/images/2018-10/img_944x629$2018_10_23_13_20_29_124325.png"
CARRO="https://www.pnglot.com/pngfile/detail/143-1438797_carro-png-imagenes-de-carros-png.png"
class yuri():
    pista=Cena(img=PISTA)
    carro=Elemento(img=CARRO)
    carro.entra(pista)
    pista.vai()
yuri()    