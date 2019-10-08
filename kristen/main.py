# kathleen.kristen.main.PY
from _spy.vitollino.main import Cena, Elemento,Labirinto
from _spy.vitollino.main import INVENTARIO as inv
ZEZINHO="https://cdn.pixabay.com/photo/2014/04/03/10/45/bodybuilding-311351_960_720.png"
CASA="https://images.vexels.com/media/users/3/137235/isolated/preview/67bd605391bf47796ff9c976879fd002-edif--cio-moderno-casa-da-cidade-by-vexels.png"
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
PAPEL="
class CARTA():
    zeze= Elemento (img=ZEZINHO)
    casinha= Cena (img=CASA)
    rosa=Elemento (img=ROSALINDA)
    cofre=Cena (img=COFRE)
    gavetinha=Elemento (img=GAVETA)
    livrinho=Elemento (img=LIVRO)
    corredor=Cena(img=CORREDOR)
    monitor=Elemento (img=MONITOR)
    portinha=Elemento (img=PORTINHA)
    salinha=Cena (img=LABORATORIO)
    dr=Elemento (img=DR_HAMSTER)
    fio=Labirinto(N=casinha,S=cofre,O=
    zeze.entra(casinha)
    rosa.entra(casinha)
    casinha.vai()
    zeze.entra(corredor)
    corredor.vai()
    zeze.entra(salinha)
    dr.entra(salinha)
    salinha.vai()
    rosa.entra(salinha)
    salinha.vai()
    casinha.esquerda=corredor
    corredor.direita=casinha
    corredor.esquerda=salinha
    salinha.direita=corredor
    salinha.esquerda=casinha
    casinha.direita=salinha
    CARTA()