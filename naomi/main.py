# kathleen.naomi.main.py
from _spy.vitollino.main import Cena, Elemento 
from _spy.vitollino.main import INVENTARIO as inv

CENA = "https://3.bp.blogspot.com/-xsgQSKi0xHg/V1IMCh9vlqI/AAAAAAAAEDw/S81m4JHTNdYOrdQvm_GLEXt2eqVr8NoNgCLcB/s1600/pngg.png"
BONECA = "https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_boneco_homem_de_ferro_iron_man_mark_lxxxv_vingadores_ultimato_avengers_endgame_mms528_d30__42292_1_20190402112855.png"
class OI():
		#def _init_main (self)
		cena = Cena ( img = CENA )
		 boneca = Elemento ( img = BONECA )
		boneca.entra(cena)
		cena.vai()
         
OI() 