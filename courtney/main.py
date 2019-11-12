# kathleen.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as invi
INDIO = "https://cdn.pixabay.com/photo/2019/03/14/21/55/apache-4056009_960_720.png"
MATO = "https://wowf.com.br/wp-content/uploads/2019/03/ilustracao-768x384.png"
TARTARUGA = "https://toppng.com/public/uploads/preview/tartaruga-ninja-vermelho-11550709278xvmk3b5qhi.png"
BECO = "https://micosemental.wordpress.com/files/2009/11/beco.png"
LADRAO = "https://cdn.pixabay.com/photo/2017/01/30/21/48/burglar-2022159_960_720.png"
class JohnnyLindo()
    mato=Cena(img=MATO)
    indio=Elemento(img=INDIO)
    beco=Cena(img=BECO)
    tartaruga=Elemento(img=TARTARUGA)
    ladrao=Elemento(img=LADRAO)
    mato.direita=indio
    beco.esquerda=tartaruga, ladrao
    ladrao.vai()
JohnnyLindo()