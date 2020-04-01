# kathleen.ruzwana.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Sala
from _spy.vitollino.main import Inventario as inv
DOENTE="https://i.imgur.com/OZcZ7uk.png"
AJUDANTE="https://i.imgur.com/jfJRkQ0.png"
CIENTISTA="https://i.imgur.com/j9dFKoh.png"
LADRAO="https://i.imgur.com/NcNFUxj.png"
CAES="https://i.imgur.com/vzFSVpa.png"
BIBLIOTECA="tps://i.imgurht.com/nNdvZpp.jpg"
CASA="https://i.imgur.com/yAdeiPL.png"
COMPUTADOR="https://i.imgur.com/Sh1qCg8.png"
REMEDIO="https://i.imgur.com/KP8tH8m.png"
PORTA="https://i.imgur.com/tb356So.png"
GUARDAS="https://images.vexels.com/media/users/3/163203/isolated/preview/1091d5c6064085d74145f6ae567b3880-homem-arma-seguran--a-ilustra----o-by-vexels.png"
LIVRO="https://static3.tcdn.com.br/img/img_prod/280297/2276_1_20170803132328.jpg"
LABORATORIO="http://casaamericana.com.br/wp-content/uploads/2018/05/4-problemas-que-afetam-a-produtividade-no-laboratorio.png"
TUNEL="https://www.dm.com.br/wp-content/uploads/2018/08/Sisenando-Francisco-de-Azevedo-2.jpg"
SAIDA="https://i.imgur.com/hwV0ofX.jpg"
LIXO="https://cdn.pixabay.com/photo/2016/10/03/19/00/garbage-1712516_960_720.png"
MAPA="https://pngimage.net/wp-content/uploads/2018/06/mapa-desenho-png-3.png"
BILHETE="https://i.imgur.com/lv86Znb.png"
PORTAO="https://i.imgur.com/AfB9mWY.png"
PRACA="https://i.imgur.com/kkiaSmf.png"
class leni():
    caes=Elemento(img=CAES)
    guardas=Elemento(img=GUARDAS)
    remedio=Elemento(img=REMEDIO)
    mapa=Elemento(img=MAPA)
    computador=Elemento(img=COMPUTADOR)
    lixo=Elemento(img=LIXO)
    porta=Elemento(img=PORTA)
    livro=Elemento(img=LIVRO)
    bilhete=Elemento(img=BILHETE)
    portao=Elemento(img=PORTAO)
    saida=Elemento(img=SAIDA)
    biblioteca=Cena(img=BIBLIOTECA)
    casa=Cena(img=CASA)
    laboratorio=Cena(img=LABORATORIO)
    tunel=Cena(img=TUNEL)
    portao=Cena(img=PORTAO)
    pracinha=Cena(img=PRACA)
    haha=Labirinto(norte=casa,sul=biblioteca,oeste=laboratorio,leste=porta)
    hehe=Labirinto(leste=porta,sul=tunel,oeste=portao,norte=casa)
    doente=Elemento(img=DOENTE)
    doente.entra (casa)
    faladoente=Texto(casa,"o que aconteceu?")
    doente.vai=faladoente.vai
    ajudante=Elemento(img=AJUDANTE)
    ajudante.entra(norte.casa)
    falaajudante=Texto(casa,"O cientista foi sequetrado e roubaram as escrituras e seu compuatdor")
    ajudante.vai=falaajudante.vai
    #falaajudante=Texto(casa,"Sua primeira missão é achar os comprimidos para que ele fique estável até você encontrar o cientista")
    #ajudante.vai=falaajudante.vai
    
    ladrao=Elemento= (LADRAO)
    ladrao.entra(norte.casa)
    
    ajudante.entra(sul.biblioteca)
    falaajudante=Texto(biblioteca,"As coordenadas para seu rémedio estão no genótipo de uma doença")
    ajudante.vai=falaajudante.vai
    #falaajudante=Texto(biblioteca,"Todas as informações estão guardadas na biblioteca")
    #ajudante.vai=falaajudante.vai
    
    doente.entra(sul.biblioteca)
    bilhete.entra(sul.biblioteca)
    falabilhete=Texto(biblioteca,"Sua corordenada é hemofila!")
    bilhete.vai=falabilhete.vai
    guardas.entra(sul.biblioteca)
    livro.entra(sul.biblioteca)
    
    cientista=Elemento(img=CIENTISTA)
    cientista.entra(oeste.laboratorio)
    
    doente.entra(oeste.laboratorio)
    ladrao.entra(oeste.laboratorio)
    ajudante.entra(oeste.laboratorio)
    falaajudante=Texto(laboratorio,"doençança onde não há ou há pouca produção de melanina")
    ladrao.entra(leste.porta)
    doente.entra(leste.porta)
    cientista.entra(oeste.laboratorio)
    falacientista=Texto(laboratorio,"Foi meu ajudante que roubou as escrituras e me sequestrou!!")
    doente.entra(sul.tunel)
    cientista.entra(sul.tunel)
    saida.entra(oestte.portao)
    doente.entra(oeste.portao)
    cientista.entra(oeste.portao)
    doente.entra(leste.pracinha)
    cientista.entra(leste.pracinha)
    #hehe.vai()
    haha.vai()
leni()
        
        
