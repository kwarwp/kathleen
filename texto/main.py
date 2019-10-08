# kathleen.texto.main.py
from _spy.vitollino.main import Texto


class TextOpt(Texto):
    def __init__(self, cena=NADA, tit="", txt="", foi=None, **kwargs):
        super().__init__(None, tit=tit, txt=txt, vai=None, **kwargs)
        self.optou = None
        self.monta_optar(**kwargs)
    

    def monta_optar(self, **kwargs):
        def opcao(letra):
            self.optou = letra

            def opta(letra, texto):
                div = html.DIV(Class="content")
                optou = html.A(chr(ABOXED + ord(letra) - ord("A")), Class="option", href="#")
                optou.onclick = lambda *_: opcao(letra) or self._close()
                texto_opcao = html.SPAN(texto)
                div <= optou
                div <= texto_opcao
                return div

            optar = [[optou, texto] for optou, texto in kwargs.items() if optou in "ABCDEFGHIJK"]
            for op in optar:
                self.div <= opta(*op)
