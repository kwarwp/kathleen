# kathleen.lisa.main.py
from _spy.vitolino.main import Cena,Elemento,Labirinto
from _spy.vitolino.main import inventario as inv
PRAIA= "https://img.freepik.com/fotos-gratis/praia-e-mar_74190-2371.jpg?size=626&ext=jpg"
BOLA= "https://3.bp.blogspot.com/-xsgQSKi0xHg/V1IMCh9vlqI/AAAAAAAAEDw/S81m4JHTNdYOrdQvm_GLEXt2eqVr8NoNgCLcB/s1600/pngg.png"

class PARTY():
      #def __ int __(self):
        praia=Cena(img=PRAIA)
        bola=Elemento(img=BOLA)
        bola.entra(praia)
        prai.vai()      
PARTY()