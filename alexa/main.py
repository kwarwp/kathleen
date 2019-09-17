# kathleen.alexa.main.py
from _spy.vitollino.main import Cena , Elemento , Texto
from _spy.vitollino.main import INVENTARIO as inv
DOCE = "https://img.elo7.com.br/product/zoom/271238B/painel-redondo-sublimado-3d-mundo-doce-01-1-5x1-5m-mundodoce-festa-painel-sublimado.jpg"
SUGA= "https://img1.gratispng.com/20180707/far/kisspng-suga-bts-k-pop-spring-day-japanese-version-bts-suga-5b4143ffbcec70.6425521015310039037738.jpg"
class OI ():
		doce = Cena (img=DOCE)
		suga = elemento(img=SUGA)
		suga.entra(doce)
		doce.vai()
OI()