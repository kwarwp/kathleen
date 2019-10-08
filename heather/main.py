# kathleen.heather.main.py
from _spy.vittorino.main import Cena, Elemento, Labirinto, Texto
from _spy.vittorino.main import inventario as inv
ESCADA="https://png.pngtree.com/png-clipart/20190121/ourmid/pngtree-cartoon-hand-drawn-watercolor-stair-design-cartoon-hand-painted-watercolor-png-image_517547.jpg"
AJUDANTE="https://png.pngtree.com/element_origin_min_pic/16/06/14/16575fc06949b28.jpg"
GARCA="https://img1.gratispng.com/20180131/lye/kisspng-bird-crane-egret-bird-5a727ebde23183.4981214015174529899265.jpg"
REDE="www.entomologiaonline.com.br/image/cache/data/bug_catcher-350x430.jpg"
LABORATORIO="http://blog.homyquimica.com.br/wp-content/uploads/2018/02/homy-capa-07-02-1.png"
PENA="https://gartic.com.br/imgs/mural/ca/calum/pena.png"
ESTANTE="https://png.pngtree.com/element_pic/17/08/05/a809ff54a922910ecaa487b955e5d535.jpg"
LIVRO="https://png.pngtree.com/element_pic/00/16/09/0357caa9ff68093.jpg"
class SEILACARA()
    laboratorio=Cena (img=LABORATORIO, tit="laboratorio", top=50, left)
    escada=Cena (img=ESCADA)
    ajudante=elemento (img=AJUDANTE)
    garca=elemento (img=GARCA)
    estante=elemento (img=ESTANTE)
    ajudante.entra(escada)
    estante.entra(labtoratorio)
    
    

