# kathleen.sarah.main.py
from _spy.vitollino.main.import Cena , Elemento , Texto
#from _spy.vittollino.main.import
FRIO = "https://cdn.pixabay.com/photo/2014/12/15/03/09/house-568557_960_720.jpg"
BILLIE = "https://p1.hiclipart.com/preview/871/471/638/billie-eilish-woman-wearing-brown-and-red-bobble-jacket-png-clipart.jpg"
class FELICIDADE():
		frio = Cena ( img= FRIO)
		billie = Elemento ( img= BILLIE)
		billie.entra(frio)
		frio.vai()

FELICIDADE()
