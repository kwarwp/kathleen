# kathleen.naomi.main.py
from _spy.vitollino.main import Cena, Elemento 
from _spy.vitollino.main import INVENTARIO as inv

CENA = "https://3.bp.blogspot.com/-xsgQSKi0xHg/V1IMCh9vlqI/AAAAAAAAEDw/S81m4JHTNdYOrdQvm_GLEXt2eqVr8NoNgCLcB/s1600/pngg.png"
BONECA = "https://images.vexels.com/media/users/3/134449/isolated/preview/fd3c681037ff454277a744562ae002cd-boneca-da-menina-dos-desenhos-animados-by-vexels.png"
class OI ():
		#def _init_main (self)
		cena = Cena ( img = CENA )
		 boneca= Elemento (img=BONECA)
		boneca.entra(cena)
		cena.vai()
         
OI() 