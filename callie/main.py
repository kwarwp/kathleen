# kathleen.callie.main.py
from _spy.vittolino.main import Cena, Elemento, Labirinto
from _spy.vittolino.main import INVENTARIO as inv
HOMEM="https://png.pngtree.com/element_pic/17/09/15/c76996e051a875cb585bf5350d53eabe.jpg"
AJUNDANTE="https://i.pinimg.com/originals/25/48/27/254827fb621ed6c9e50b401d92554810.png"
LADRAO="https://cdn.pixabay.com/photo/2017/01/30/21/48/burglar-2022159_960_720.png"
CASA="https://www.atom.org.br/wp-content/uploads/2018/07/casas-png-casa-png-499-371-499-1.png"
CIENTISTA="https://png.pngtree.com/png-clipart/20190604/original/pngtree-the-scientist-png-image_949187.jpg"
BIBLIOTECA="https://live.staticflickr.com/30/65319105_09adc58261_z.jpg"
PORTA="https://cdn.leroymerlin.com.br/products/porta_montada_de_giro_sarrafeada_de_madeira_2,13x0,75m_concrem_wood_89822306_0001_300x300.jpg"
LIVRO="https://static3.tcdn.com.br/img/img_prod/280297/2276_1_20170803132328.jpg"
PORTA2="https://images.tcdn.com.br/img/img_prod/611678/porta_lisa_semi_solida_angelim_52_1_20190517171407.jpg"
TUNEL="https://www.dm.com.br/wp-content/uploads/2018/08/Sisenando-Francisco-de-Azevedo-2.jpg"
MAPA="https://png.pngtree.com/element_origin_min_pic/17/08/13/0637aa84ab59de81fc26e62aa117f071.jpg"

class OVO():
    homen=Elemento (img=HOMEM)
    casa= Cena (img=CASA)
    ajudante= Elemento (img=AJUDANTE)
    ladrao= Elemento (img=LADRAO)
    cientista= Elemento (img=CIENTISTA)
    biblioteca= Cena (img=BIBLIOTECA)
    porta= Cena (img=PORTA)
    livro= Elemento (img=LIVRO)
    portinha= Cena (img=PORTA2)
    tunel= Cena (img=TUNEL)
    mapinha= Elemento (img=MAPA)
    homem.entra(casa)
    livro.entra(biblioteca)
    casa.vai()
    biblioteca.vai()
    
    OVO()