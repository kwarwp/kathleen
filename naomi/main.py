# kathleen.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Sala
from _spy.vitollino.main import INVENTARIO as inv

#CENI = "https://img.freepik.com/fotos-gratis/praia-e-mar_74190-2371.jpg?size=626&ext=jpg"
BONECA = "https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_boneco_homem_de_ferro_iron_man_mark_lxxxv_vingadores_ultimato_avengers_endgame_mms528_d30__42292_1_20190402112855.png"
#HOSPITAL= "https://images.vexels.com/media/users/3/144204/isolated/preview/f6d082b22c3fbdc5d2927ff1c7cd57d4---cone-do-edif--cio-do-hospital-by-vexels.png"
BILU = "https://images.vexels.com/media/users/3/134449/isolated/preview/fd3c681037ff454277a744562ae002cd-boneca-da-menina-dos-desenhos-animados-by-vexels.png"
LILITA = "https://i.pinimg.com/originals/9c/dc/89/9cdc89263f56b697cb165edda0fcbbe1.png"
CEU= "https://png.pngtree.com/element_origin_min_pic/16/06/19/015765842a90594.jpg"
ANA = "https://i.pinimg.com/originals/91/71/39/917139b1f345b2cfeaed6fc340f896ec.png"
SALA1="https://upload.wikimedia.org/wikipedia/commons/0/0d/Corredor_da_Faculdade_de_Informa%C3%A7%C3%A3o_e_Comunica%C3%A7%C3%A3o%2C_UFG_Samambaia%2C_janeiro_de_2017.jpg"
SALA2= "https://cdn.pixabay.com/photo/2017/04/07/19/16/infinity-blue-2211659_960_720.jpg"
SALA3="https://upload.wikimedia.org/wikipedia/commons/8/82/Rodovi%C3%A1ria_de_Curvelo.jpg"
SALA4= "https://static.escolakids.uol.com.br/conteudo_legenda/74213602df7655dcb813515dbbb1c837.jpg"

class OI():
	#def _init_main (self)
    #ceni = Cena(img = CENI)
    #hospital = CE(img = HOSPITAL)
    lilita = Elemento(img = LILITA,style=dict(
    left=100, top=150, width=200, height="150px"))
    #boneca.entra(ceni)
    sala1 = Cena(img= SALA1)
    sala2 = Cena(img=SALA2)
    sala3 = Cena(img=SALA3)
    sala4 = Cena(img=SALA4)
    self.ceu= ceu= Sala ( n= SALA1, s= SALA2, o= SALA3, l= SALA4)
    
    boneca = Elemento( img = BONECA, tit = "Olá, eu sou o homem de ferro", style=dict(
    left=100, top=150, width=200, height="150px"))  
    boneca.entra(ceu.oeste)
    falaboneca = Texto(SALA3, "Hellou")
    boneca.vai = falaboneca.vai
    
    #ceni.entra(ceu.norte)
    #hospital.entra(ceu.leste)
    bilu = Elemento(img = BILU, tit = "Olá, eu sou Bilu")
    bilu.entra(ceu.leste)
    falabilu = Texto(SALA4, "Olá")
    bilu.vai = falabilu.vai
    
    ana = Elemento(img = ANA)
    ana.entra(ceu.sul)
    falaana = Texto(SALA2, "HIII")
    ana.vai = falaana.vai
    
    ceu.oeste.vai()
    ceu.vai()

OI()


