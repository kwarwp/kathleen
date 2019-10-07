# kathleen.ruzwana.main.py
from _spy.vittolino.main import Cena, Elemento , Labirinto
from _spy.vittolino.main import inventario as inv
DOENTE=""
AJUDANTE=""
CIENTISTA=""
LADRAO=""
CAES=""
BIBLIOTECA=""
CASA=""
COMPUTADOR=""
REMEDIO=""
PORTA=""
GUARDAS=""
LIVRO=""
LABORATORIO=""
PREDIO=""
TUNEL=""
SAIDA=""
LIXO=""
MAPA=""
 class leni():
    doente= Elemento(img=DOENTE)
    ajudante= Elemento(img=AJUDANTE)
    cientista= Elemento(img=CIENTISTA)
    ladrao= Elemento(img=LADRAO)
    caes= Elemento(img=CAES)
    guardas= Elemento(img=GUARDAS)
    remedio= Elemento(img=REMEDIO)
    mapa= Elemento(img=MAPA)
    computador= Elemento(img=COMPUTADOR)
    lixo= Elemento(img=LIXO)
    porta= Elemento(img=PORTA)
    livro= Elemento(img=LIVRO)
    biblioteca= Cena(img=BIBLIOTECA)
    casa= Cena (img=CASA)
    laboratorio= Cena(img=LABORATORIO)
    predio= Cena(img=PREDIO)
    tunel= Cena(img=TUNEL)
    saida= Cena(img=SAIDA)
      doente.entra(casa)
        ajudante.entra(casa)
        ladrao.entra(casa)
        ajudante.entra(biblioteca)
        doente.entra(biblioteca)
        
