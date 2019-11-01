# kathleen.natalia.main.
from _spy.vitollino.main import Cena, Elemento
from _spy.vitollino.main import Inventario as inv
ESCOLA = "https://images.educamaisbrasil.com.br/content/basico/instituicao/logo/g/colegio-ndi.png"
SALA = "http://www.adel.org.br/wp-content/uploads/2016/07/Sala-de-Aula.png"
ALUNO = "http://www.ifmg.edu.br/ceadop3/imagens/aluno.png/@@images/image.png"
PROFESSOR = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Professor.png"
class pibic():
    escola=Cena(img=ESCOLA)
    sala = Cena(img = SALA)
    professor = Elemento(img= PROFESSOR)
    aluno = Elemento(img = ALUNO)
    professor.entra(sala)
    aluno.entra(escola)
    sala.vai
    escola.vai
    pibic()   