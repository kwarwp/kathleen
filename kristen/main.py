# kathleen.kristen.main.PY
from _spy.vitollino.main import Cena, Elemento,Labirinto
from _spy.vitollino.main import INVENTARIO as inv
ZEZINHO="
CASA="
ROSALINDA="
COFRE="
LIVRO="
CORREDOR="
MONITOR=
PORTINHA=
LABORATORIO=
DR_HAMSTER=

class CARTA():
    zeze= Elemento (img=ZEZINHO)
    casinha= Cena (img=CASA)
    rosa=Elemento (img=ROSALINDA)
    cofre=Cena (img=COFRE)
    livrinho=Elemento (img=LIVRO)
    corredor=Cena(img=CORREDOR)
    monitor=Elemento (img=MONITOR)
    portinha=Cena (img=PORTA)
    salinha=Cena (img=LABORATORIO)
    dr=Elemento (img=DR_HAMSTER)
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
    
    CARTA()