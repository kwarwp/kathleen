# kathleen.rachel.main.py
from _spy.vitollino.main import Elemento, Cena, Texto
from _spy.vitollino.main import Inventario as invi 
MARTE="https://abrilsuperinteressante.files.wordpress.com/2019/05/site_marte.png"
MINIOS="https://imagensemoldes.com.br/wp-content/uploads/2018/05/Meu-Malvado-Favorito-Minions-Jerry-4-PNG.png"
MORTI="https://i.pinimg.com/originals/57/79/e9/5779e9e8c85f594eae72c8f5b6ba0d23.png"
HUCK="http://www.pngall.com/wp-content/uploads/2016/03/Avengers-Hulk-PNG.png"
MATO="https://pngimage.net/wp-content/uploads/2018/06/mato-png-2.png"
BARATA="https://pngimage.net/wp-content/uploads/2018/05/barata-voadora-png-1-280x200.png"
BRUXA=
class peixe ():
    marte=Cena(img=MARTE)
    morti=Cena(img=MORTI)
    mato=Cena(img=MATO)
    barata=Elemento(img=BARATA)
    barata.entra(mato)
    minios=Elemento(img=MINIOS)
    minios.entra(marte)
    huck=Elemento(img=HUCK)
    huck.entra(morti)
    marte.direita=morti
    morti.esquerda=marte
    barata.esquerda=mato
    morti.direita=mato    
    marte.vai()
    
peixe()