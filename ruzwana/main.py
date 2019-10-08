# kathleen.ruzwana.main.py
from _spy.vittolino.main import Cena, Elemento, Labirinto, Texto
from _spy.vittolino.main import inventario as inv
DOENTE="https://png.pngtree.com/element_pic/17/09/15/c76996e051a875cb585bf5350d53eabe.jpg"
AJUDANTE="https://i.pinimg.com/originals/25/48/27/254827fb621ed6c9e50b401d92554810.png"
CIENTISTA="https://png.pngtree.com/png-clipart/20190604/original/pngtree-the-scientist-png-image_949187.jpg"
LADRAO="https://cdn.pixabay.com/photo/2017/01/30/21/48/burglar-2022159_960_720.png"
CAES=""
BIBLIOTECA="https://live.staticflickr.com/30/65319105_09adc58261_z.jpg"
CASA="https://www.atom.org.br/wp-content/uploads/2018/07/casas-png-casa-png-499-371-499-1.png"
COMPUTADOR=""
REMEDIO=""
PORTA="https://cdn.leroymerlin.com.br/products/porta_montada_de_giro_sarrafeada_de_madeira_2,13x0,75m_concrem_wood_89822306_0001_300x300.jpg"
GUARDAS=""
LIVRO="https://static3.tcdn.com.br/img/img_prod/280297/2276_1_20170803132328.jpg"
LABORATORIO=""
TUNEL="https://www.dm.com.br/wp-content/uploads/2018/08/Sisenando-Francisco-de-Azevedo-2.jpg"
SAIDA=""
LIXO=""
MAPA="https://png.pngtree.com/element_origin_min_pic/17/08/13/0637aa84ab59de81fc26e62aa117f071.jpg"
BILHETE=""
PORTAO=""
PRACA=""
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
    bilhete= Elemento(img=BILHETE)
    portao= Elemento(img=PORTAO)
    biblioteca= Cena(img=BIBLIOTECA)
    casa= Cena (img=CASA)
    laboratorio= Cena(img=LABORATORIO)
    tunel= Cena(img=TUNEL)
    saida= Cena(img=SAIDA)
    pracinha= Cena(img=PRACA)
    haha= Labirinto(N=casa,S=biblioteca,O=laboratorio,L=porta)
    hehe= Labirinto(N=porta,S=tunel,O=saida,L=pracinha)
        doente.entra(casa)
        faladoente= Texto(casa,"o que aconteceu?")
        doente.vai=falapeixinho.vai
        ajudante.entra(casa)
        falaajudante=texto(casa"o cientista foi sequetrado e roubaram as escrituras e seu compuatdor")
        ajudante.vai=falaajudante.vai
        falaajudante=Texto(casa" Sua primeira missão é achar os comprimidos para que ele fique estável até você encontrar o cientista")
        ajudante.vai=falaajudante.vai
        ladrao.entra(casa)
        ajudante.entra(biblioteca)
        falaajudante=Texto(biblioteca" As coordenadas para seu rémedio estão no genótipo de uma doença")
        ajudante.vai=falaajudante.vai
        falaajudante=Texto(biblioteca"Todas as informações estão guardadas na biblioteca")
        ajudante.vai=falaajudante.vai
        doente.entra(biblioteca)
        bilhete.entra(biblioteca)
        falabilhete=Texto(biblioteca"Sua coordenada é hemofilia")
        bilhete.vai=falabilhete.vai
        guardas.entra(biblioteca)
        livro.entra(biblioteca)
        cientista.entra(laboratorio)
        doente.entra(laboratorio)
        ladrao.entra(laboratorio)
        ajudante.entra(laboratorio)
        falaajudante=Texto(laboratorio"Doença onde não há ou há pouca produção de melanina")
        ladrao.entra(porta)
        doente.entra(porta)
        cientista.entra(porta)
        
        ladrao.entra(tunel)
        doente.entra(tunel)
        cientista.entra(tunel)
        doente.entra(pracinha)
        cientista.entra(pracinha)
        
        
        
        
