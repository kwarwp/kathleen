# kathleen.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Sala
from _spy.vitollino.main import INVENTARIO as inv

CENA = "https://img.freepik.com/fotos-gratis/praia-e-mar_74190-2371.jpg?size=626&ext=jpg"
BONECA = "https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_boneco_homem_de_ferro_iron_man_mark_lxxxv_vingadores_ultimato_avengers_endgame_mms528_d30__42292_1_20190402112855.png"
HOSPITAL= "https://images.vexels.com/media/users/3/144204/isolated/preview/f6d082b22c3fbdc5d2927ff1c7cd57d4---cone-do-edif--cio-do-hospital-by-vexels.png"
CEU= "https://png.pngtree.com/element_origin_min_pic/16/06/19/015765842a90594.jpg"
SALA1="https://upload.wikimedia.org/wikipedia/commons/0/0d/Corredor_da_Faculdade_de_Informa%C3%A7%C3%A3o_e_Comunica%C3%A7%C3%A3o%2C_UFG_Samambaia%2C_janeiro_de_2017.jpg"
SALA2= "https://cdn.pixabay.com/photo/2017/04/07/19/16/infinity-blue-2211659_960_720.jpg"
SALA3="https://upload.wikimedia.org/wikipedia/commons/8/82/Rodovi%C3%A1ria_de_Curvelo.jpg"
SALA4= "https://static.escolakids.uol.com.br/conteudo_legenda/74213602df7655dcb813515dbbb1c837.jpg"

class OI():
	#def _init_main (self)
    cena = Cena ( img = CENA )
    boneca = Elemento ( img = BONECA, style=dict(
    left=100, top=150, width=200, height="150px"))  
    boneca.entra(cena)
    self.ceu= ceu= Sala ( n= SALA1, s= SALA2, o= SALA3, l= SALA4)
    boneca.entra(oeste.Sala3)
    cena.entra(norte.Sala1)
    hospital.entra(leste.Sala4)
    ceu.vai()

OI()


