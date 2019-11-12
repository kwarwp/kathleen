# kathleen.rachel.main.py
from _spy.vitollino.main import Elemento, Cena, Texto
from _spy.vitollino.main import Inventario as invi 
MARTE="https://abrilsuperinteressante.files.wordpress.com/2019/05/site_marte.png"
MINIOS="https://imagensemoldes.com.br/wp-content/uploads/2018/05/Meu-Malvado-Favorito-Minions-Jerry-4-PNG.png"
MORTI="https://png.pngtree.com/png-clipart/20190611/original/pngtree-vector-fog-png-image_2120607.jpg"
HUCK="http://www.pngall.com/wp-content/uploads/2016/03/Avengers-Hulk-PNG.png"
class peixe ():
    marte=Cena(img=MARTE)
    morti=Cena(img=MORTI)
    minios=Elemento(img=MINIOS)
    minios.entra(marte)
    huck=Elemento(img=HUCK)
    huck.entra(morti)
    marte.direita=morti
    morti.esquerda=marte
    marte.vai()
peixe()