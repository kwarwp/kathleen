# kathleen.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as invi
CIENTISTA = "https://img2.gratispng.com/20180515/ree/kisspng-mad-scientist-famous-scientists-clip-art-5afaa2c000e336.8963581315263751040036.jpg"
SANGUE = "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/14126.png"
BIBLIOTECA = "https://daequfpr.files.wordpress.com/2012/04/biblioteca3.jpg"
CENTROI = "https://www.itforum365.com.br/wp-content/uploads/2017/08/prescriptive-soc.png"
SETA = "https://image.flaticon.com/icons/png/512/2026/2026737.png"
PORTA = "https://cdn.pixabay.com/photo/2014/12/21/23/45/door-575962_960_720.png"
FRAGMENTO = "https://png.pngtree.com/png-clipart/20190117/ourlarge/pngtree-c4d-purple-decoration-triangle-block-png-image_426001.jpg"
DNA = "https://mpng.pngfly.com/20190508/qs/kisspng-dna-scalable-vector-graphics-computer-icons-gene-kaznmu-kz-pictures-to-pin-on-pinterest-5cd2d75921b124.839995971557321561138.jpg"
PROTEINA = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Mouse_cholera_antibody.png/170px-Mouse_cholera_antibody.png"
MOLECULA = "https://images.vexels.com/media/users/3/159421/isolated/preview/e2739354640fee942f38f6283db269e6-c--lula-de-modelo-de-mol--cula-plana-by-vexels.png"
GENE = "http://wiki.bacterialtakeover.com/images/2/20/Gene_strand.png"
ATOMOS = "https://img2.gratispng.com/20181120/he/kisspng-vector-graphics-atomic-nucleus-atomsymbol-atom-icons-925-free-vector-icons-5bf4afc71916b8.7770408515427624391028.jpg"
BANCADA = "https://cdn.pixabay.com/photo/2014/12/21/23/44/counter-575937_960_720.png"
class yato ():
    def blibleotec ():
        bibleoteca= Cena(img=BIBLIOTECA)
        sangue= Elemento(img=SANGUE)
        cientista= Elemento(img=CIENTISTA)
        sangue.entra(bibleoteca)
        cientista.entra(bibleoteca)
        bliblioteca.vai()
    def centru ():
        centro= Cena(img=CENTROI)
        cientista= Elemento(img=CIENTISTA)
        seta= Elemento(img=SETA)
        porta= Elemento(img=PORTA)
        bancada= Elemento(img=BANCADA)
        dna= Elemento(img=DNA)
        proteina= Elemento(img=PROTEINA)
        molecula= Elemento(img=MOLECULA)
        gene= Elemento(img=GENE)
        atomos= Elemento(img=ATOMOS)
        cientista.entra(centro)
        seta.entra(centro)
        porta.entra(centro)
        centro.vai()
yato.vai()
        