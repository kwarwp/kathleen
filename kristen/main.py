# kathleen.kristen.main.py
from _spy.vitollino.main import Cena, Elemento,Labirinto
from _spy.vitollino.main import INVENTARIO as inv
ZEZINHO="https://cdn.pixabay.com/photo/2014/04/03/10/45/bodybuilding-311351_960_720.png"
CASA="https://banner2.kisspng.com/20180529/wpo/kisspng-home-living-room-apartment-house-bedroom-5b0de1b6bd2448.4022608015276364067747.jpg"
ROSALINDA="https://cdn3.iconfinder.com/data/icons/indian-woman-professions/512/21-512.png"
COFRE="http://1.bp.blogspot.com/-yWkpr4XDKOE/UzRYYgSXO6I/AAAAAAAAdTY/dLHe6tf6COM/s1600/cofre-em-png-queroimagem-cei%C3%A7a-crispim+(1).png"
LIVRO="https://www.conceicaodabarra.es.leg.br/imagens/livro.png/image_preview"
CORREDOR="http://portal.utfpr.edu.br/cursos/coordenacoes/stricto-sensu/ppg-ee-cp/area-academica/laboratorios-e-infra-estrutura-1/corredor.png/@@images/2427c4e2-7e87-4f01-8718-16c6dd509536.png"
MONITOR="https://mpng.pngfly.com/20180208/suw/kisspng-computer-monitor-led-backlit-lcd-personal-computer-tv-pc-5a7be1c8b44e89.5652564315180681687386.jpg"
PORTINHA="https://png.pngtree.com/png-clipart/20190611/original/pngtree-vector-painted-open-door-png-image_2564653.jpg"
LABORATORIO="http://www.hemocito.com.br/wp-content/uploads/2016/06/servicos-laboratorio.png"
DR_HAMSTER="https://i.pinimg.com/736x/33/34/86/333486c9286ae9acb54ac214594326dd.jpg"
REMEDIO="https://png.pngtree.com/png-clipart/20190603/original/pngtree-medicine-png-image_486130.jpg"
GAVETA="http://clipart.coolclips.com/480/vectors/tf05276/CoolClips_vc047763.png"
ESTANTE="https://png.pngtree.com/element_pic/17/08/05/a809ff54a922910ecaa487b955e5d535.jpg"
QUADRO="https://img2.gratispng.com/20180131/yjw/kisspng-chess-window-square-picture-frame-pattern-maroon-border-frame-png-hd-5a721c5a89b177.262021501517427802564.jpg"
QUADRO2="https://3.bp.blogspot.com/-l_N1GilZmaE/Wmu1nOjhybI/AAAAAAAAepk/ZrLoM5ihZXgh8_XYckqNar5WBQypyiNLQCLcBGAs/s1600/Quadro%2Btorto.PNG"
PAPEL="http://1.bp.blogspot.com/-2ZRwuDRFsUE/UN26nlcbvYI/AAAAAAAAAaQ/5_I8JJscq4o/s1600/paper1.png"
COFRINHO="https://images.tcdn.com.br/img/img_prod/448593/cofre_digital_bh_d23_hotel_grande_br_4680_1_20180420145844.png"

class CARTA():
    def __init__(self):
    casa=Cena (img=CASA)
    zeze=Elemento (img=ZEZINHO)
    rosa=Elemento (img=ROSALINDA)
    quadro=Elemento (img=QUADRO)
    zeze.entra (casa)
    rosa.entra (casa)
    quadro.entra (casa)
    casa.vai()
    
    corredor=Cena (img=CORREDOR)
    quadro2=Elemento (img=QUADRO2)
    quadro2.entra(corredor)
    corredor.vai()
    
    cofre=Cena (img=COFRE)
    gaveta=Elemento (img=GAVETA)
    papel=Elemento (img=PAPEL)
    gaveta.entra(cofre)
    papel.entra (cofre)
    cofre.vai()
    
    estante=Cena (img=ESTANTE)
    casa=Cena (img=CASA)
     casa.vai()
    
CARTA()
    