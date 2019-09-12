# kathleen.kristen.main.py
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import Inventario as inv
PEAK= "https://cdn-www.bluestacks.com/bs-images/Cape-Town-1024x546.png"
PERSONAGEM="http://pm1.narvii.com/6818/931c7880be7d3bb519fabee566c918687e4b75e2v2_00.jpg"
class PLATINA():
    peak=Cena(img=PEAK)
    personagem=Elemento(img=PERSONAGEM)
    personagem.entra(peak)
    peak.vai()
    PLATINA()
    