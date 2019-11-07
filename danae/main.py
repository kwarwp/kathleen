# kathleen.danae.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import inventario as inv
CIENTISTA="https://2.bp.blogspot.com/-380MYApQgg0/T_CU1Iy8f9I/AAAAAAAAFKs/9X5_tDN93YU/s1600/Professor+Hubert+Farnsworth.png"
AJUDANTE="https://pngimage.net/wp-content/uploads/2018/06/personagens-png-4.png"
LABORATORIO="https://s03.video.glbimg.com/x720/7727950.jpg"
JARDIM=""
CAIXADEMUSICA=""
HOLOGRAMA=""
JOGADOR=""
HOSPITAL=""
ANTIDOTO=""
PAREDE=""
SETASFLORESCENTES=""
 class leni():
    cientista= Elemento(img=CIENTISTA)
    ajudante= Elemento(img=AJUDANTE)
    caixinha= Elemento(img=CAIXADEMUSICA)
    jogador= Elemento(img=JOGADOR)
    holograma= Elemento(img=HOLOGRAMA)
    antidoto= Elemento(img=ANTIDOTO)
    setinhas= Elementos(img=SETASFLORESCENTES)
    laboratorio= Cena(img=LABORATORIO)
    jardim= Cena(img=JARDIM)
    hospital= Cena(img=HOSPITAL)
    parede= Cena(img=PAREDE)
    cientista.entra(laboratorio)
    ajudante.entra(laboratorio)
    laboratorio.vai()
leni()