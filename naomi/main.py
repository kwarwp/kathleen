# kathleen.naomi.main.py
from _spy.vitollino.main import Cena, Elemento 
from _spy.vitollino.main import INVENTARIO as inv

CENA = "https://img.freepik.com/fotos-gratis/praia-e-mar_74190-2371.jpg?size=626&ext=jpg"
BONECA = "https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_boneco_homem_de_ferro_iron_man_mark_lxxxv_vingadores_ultimato_avengers_endgame_mms528_d30__42292_1_20190402112855.png"
class OI():
		#def _init_main (self)
		cena = Cena ( img = CENA )
		boneca = Elemento ( img = BONECA, style=dict(
            left=100, top=150, width=200, height="150px"))  
		boneca.entra(cena)
		cena.vai()
           
         
         
OI() 
GABINETE = "https://i.imgur.com/dp2Gnak.png"
DELEGACIA = "https://image.flaticon.com/icons/png/512/551/551512.png"
FESTA = "https://img.freepik.com/vetores-gratis/silhueta-de-um-publico-de-festa_1048-9714.jpg?size=626&ext=jpg"
CEMITERIO = "https://images.vexels.com/media/users/3/130673/isolated/preview/c58973769fe0badffc8ec348fe555f20---cone-do-cemit--rio-by-vexels.png"
DELEGADO = "https://images.vexels.com/media/users/3/158713/isolated/preview/7ad4403a507c6cf10d9d34093f6fa690-ilustra----o-uniforme-de-policial-by-vexels.png"
MORDOMO = "http://clipart.coolclips.com/480/vectors/tf05165/CoolClips_vc009999.png"
POLITICO = "https://pngimage.net/wp-content/uploads/2018/06/politico-png-6.png"
HOMEM = "https://thumbs.dreamstime.com/t/homem-negro-novo-que-sorri-contra-o-fundo-branco-96739013.jpg"
PASSISTA = "https://images.vexels.com/media/users/3/151285/isolated/preview/43ea02778621af6aca3631f2ba619bf5-mulher-carnaval-dan--ar-by-vexels.png"

