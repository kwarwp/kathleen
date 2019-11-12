# kathleen.grace.main.py
from _spy.vitollino.main import Cena,Elemento,Labirinto e Texto
from _spy.vitollino.main import INVENTARIO as inv
PIRANHA="http://www.pngmart.com/files/7/Piranha-PNG-Free-Download.png"
ESPACO="https://img2.gratispng.com/20180420/yie/kisspng-light-andromeda-galaxy-outer-space-sky-cosmos-5ad9df10333e65.6204317315242278562099.jpg" 
INES="http://3.bp.blogspot.com/-rgWJgYjJV7I/UPtVOtHWsfI/AAAAAAAAAB8/StaiQ21jcTA/s1600/2012-12-13-ines-brasil-bbb-13-babado-e-confusao-querida-6.png"
IGREJA="https://i.pinimg.com/originals/d6/48/be/d648be937077a693a2fcb0ef50a942ef.png"
CORINGA="https://www.epgrupo.com.br/wp-content/uploads/coringa-216x300-1-216x300.png"
CASADABARBIE="https://www.mundodomarketing.com.br/mundodomarketing//images/materias/casa-da-barbie.jpg"
class bruninha ():
    espaco=Cena(img=ESPACO)
    igreja=Cena(img=IGREJA)
    casadabarbie=Cena(img=CASADABARBIE)
    espaco.direita=igreja
    igreja.esquerda=espaco
    igreja.direita=casadabarbie
    casadabarbie.esquerda=igreja
    piranha=Elemento(img=PIRANHA)
    ines=Elemento(img=INES)
    coringa=Elemento(img=CORINGA)
    piranha.entra(espaco)
    ines.entra(igreja)
    coringa.entra(casadabarbie)
    espaco.vai()
bruninha()