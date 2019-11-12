# kathleen.rachel.main.py
from _spy.vittolino.main import Elemento, Cena, Texto
from _spy.vittolino.main import Inventario as invi 
MARTE = "https://abrilsuperinteressante.files.wordpress.com/2019/05/site_marte.png"
MINIOS = "https://imagensemoldes.com.br/wp-content/uploads/2018/05/Meu-Malvado-Favorito-Minions-Jerry-4-PNG.png"
MORTI = "https://png.pngtree.com/png-clipart/20190611/original/pngtree-vector-fog-png-image_2120607.jpg"
HUCK = "http://www.pngall.com/wp-content/uploads/2016/03/Avengers-Hulk-PNG.png"
class peixe ():
    arte=Cena(img=MARTE)
    minios=Elemento(img=MINIOS)
    minios.entra(arte)
    arte.direita=mort
    mort=Cena(img=MORTI)
    juck=Elemento(img=HUCK)
    JUCK.entra(mort)
    mort.esquerda=arte
    arte.entra()
peixe()