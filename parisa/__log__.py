
{'date': 'Wed Sep 04 2019 10:17:30.647 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  ifni infbn inrinfb o9ro imo
        ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 08 2019 12:48:40.844 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  inicio = Cena(img = INICIO)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Oct 08 2019 12:51:03.619 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 6
    class OI():
  module <module> line 12
    MENSAGENS.vai()
AttributeError: 'list' object has no attribute 'vai'
'''},