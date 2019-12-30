# kathleen.danae.main.
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import INVENTARIO as inv
CIENTISTA="https://2.bp.blogspot.com/-380MYApQgg0/T_CU1Iy8f9I/AAAAAAAAFKs/9X5_tDN93YU/s1600/Professor+Hubert+Farnsworth.png"
AJUDANTE="https://pngimage.net/wp-content/uploads/2018/06/personagens-png-4.png"
LABORATORIO="https://s03.video.glbimg.com/x720/7727950.jpg"
JARDIM="https://www.decorfacil.com/wp-content/uploads/2018/05/20180523plantas-para-jardim.jpg"
CAIXADEMUSICA=""
BIBLIOTEA=""
CAMERAV=""
PORTA="https://png.pngtree.com/png-clipart/20190611/original/pngtree-vector-painted-open-door-png-image_2564653.jpg"
BANCADA=""
HOSPITAL="https://midiastm.gazetaonline.com.br/_midias/jpg/2019/09/05/fernando_madeira-6299927.jpg"
class leni():
    cientista= Elemento(img=CIENTISTA)
    ajudante= Elemento(img=AJUDANTE)
    caixinha= Elemento(img=CAIXADEMUSICA)
    laboratorio= Cena(img=LABORATORIO)
    jardim= Cena(img=JARDIM)
    hospital= Cena(img=HOSPITAL)
    cientista.entra(laboratorio)
    ajudante.entra(laboratorio)
    laboratorio.vai()
leni()