# kathleen.sarah.main.py
from _spy vitollino.main import Cena, Elemento
from _spy vitollino.main import INVENTARIO as inv
PROFESSOR ="https://images.vexels.com/media/users/3/128130/isolated/preview/686ab100dddd65fc0ea71e7bb4c3db6f-senhora-professora-dos-desenhos-animados-by-vexels.png"
ALUNO="https://myrealdomain.com/images/alunos-png.png"
SALA="https://cdn.pixabay.com/photo/2018/09/30/11/55/white-board-3713307_960_720.png"
ESCOLA="http://www.kademi.com.br/images/external_layout/escola.png"
class pibic():
    professor=Elemento(img=PROFESSOR)
    aluno=Elemento(img=ALUNO)
    sala=Cena(img=SALA)
    escola=Cena(img=ESCOLA)
    aluno.entra(escola)
    professor.entra(aula)
    escola.vai()
    aula.vai()
pibic()