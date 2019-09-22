# kathleen.morgan.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto
from _spy.vitollino.main import Inventario as inv


GABINETE = "https://i.imgur.com/dp2Gnak.png"
DELEGACIA = "https://image.flaticon.com/icons/png/512/551/551512.png"
FESTA = "https://img.freepik.com/vetores-gratis/silhueta-de-um-publico-de-festa_1048-9714.jpg?size=626&ext=jpg"
CEMITERIO = "https://images.vexels.com/media/users/3/130673/isolated/preview/c58973769fe0badffc8ec348fe555f20---cone-do-cemit--rio-by-vexels.png"
DELEGADO = "https://images.vexels.com/media/users/3/158713/isolated/preview/7ad4403a507c6cf10d9d34093f6fa690-ilustra----o-uniforme-de-policial-by-vexels.png"
MORDOMO = "http://clipart.coolclips.com/480/vectors/tf05165/CoolClips_vc009999.png"
POLITICO = "https://pngimage.net/wp-content/uploads/2018/06/politico-png-6.png"
HOMEM = "https://thumbs.dreamstime.com/t/homem-negro-novo-que-sorri-contra-o-fundo-branco-96739013.jpg"
PASSISTA = "https://images.vexels.com/media/users/3/151285/isolated/preview/43ea02778621af6aca3631f2ba619bf5-mulher-carnaval-dan--ar-by-vexels.png"


class TORDO():
      #def __ int __(self):
        festa = Cena ( img = FESTA  )
        gabinete = Cena ( img = GABINETE )
        delegacia = Cena ( img = DELEGACIA )
        cemiterio = Cena ( img = CEMITERIO )
        delegado = Elemento ( img = DELEGADO )
        mordomo = Elemento ( img = MORDOMO )
        politico = Elemento ( img = POLITICO )
        homem = Elemento ( img = HOMEM )
        passista = Elemento ( img = PASSISTA )
        lugar = Labirinto (n= GABINETE, l= FESTA, o= DELEGACIA, s= CEMITERIO)
        
        delegado.entra(lugar.norte)
        mordomo.entra(lugar.norte)
        politico.entra(lugar.norte)
        lugar.norte.vai()
        
        passista.entra(lugar.leste)
        mordomo.entra(lugar.leste)
        homem.entra(lugar.leste)
        lugar.leste.vai()
        
        homem.entra(lugar.oeste)
        lugar.oeste.vai()
        
        homem.entra(lugar.sul)
        mordomo.entra(lugar.sul)
        politico.entra(lugar.sul)
        delegado.entra(lugar.sul)
        lugar.sul.vai()
        
TORDO()
        
        
