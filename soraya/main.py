# kathleen.soraya.main.py
from _spy.vitolino.main import Cena, Elemento, Labirinto, Texto
from _spy.vitolino.main import INVENTARIO as inv
BRASAO="https://www.google.com/search?q=logo+do+bras%C3%A3o+da+biblioteca+da+fiocruz+rj&rlz=1C1EKKP_enBR777BR790&sxsrf=ACYBGNQRC484CK31caMpVhXw_Us1OwMNQw:1569244371251&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimr8HqgufkAhUQF7kGHUxuA3sQ_AUIEigB&biw=1366&bih=657#imgrc=rTN3Q9NzE4cbhM:"
BIBLIOTECA="https://www.google.com/search?rlz=1C1EKKP_enBR777BR790&biw=1366&bih=657&tbm=isch&sxsrf=ACYBGNSBl7wu-8KMS5c_GeRhqEZaWFMTbg%3A1569244448111&sa=1&ei=IMWIXbq2BrmV5OUPwLa_sAg&q=biblioteca+da+fiocruz&oq=biblioteca+da+fiocruz&gs_l=img.3..35i39j0i24.6308.6695..6965...0.0..0.113.307.1j2......0....1..gws-wiz-img.iGpBZanCluk&ved=0ahUKEwi6xpSPg-fkAhW5CrkGHUDbD4YQ4dUDCAc&uact=5#imgrc=j17nfNnNZnXWmM:"
CABECA="https://www.google.com/search?rlz=1C1EKKP_enBR777BR790&biw=1366&bih=657&tbm=isch&sxsrf=ACYBGNQL_gc2m1sliSe-WeZg9KldwWGqhA%3A1569244455975&sa=1&ei=J8WIXfqRO5-d5OUPlOKksAU&q=quebra+cabe%C3%A7a+de+dna&oq=quebra+cabe%C3%A7a+&gs_l=img.3.0.35i39j0l9.192965.197693..199334...1.0..3.266.3049.10j15j2......0....1..gws-wiz-img.....10..35i362i39.eskYf_J90jY#imgrc=_nhn-rWAE6c-pM:"
JARDIM="https://www.google.com/search?rlz=1C1EKKP_enBR777BR790&biw=1366&bih=657&tbm=isch&sxsrf=ACYBGNQP-v3hSW6dfGEtHN_xZBfI5_OeQg%3A1569244656285&sa=1&ei=8MWIXaKFEd_C5OUP5cyX4AU&q=jardim+na+biblioteca+fiocruz&oq=jar&gs_l=img.3.0.35i39j0i67l2j0l7.64589.66641..68493...1.0..4.151.2121.11j9......0....1..gws-wiz-img.....10..35i362i39.sr6rDG7EXrY#imgrc=VpfF7GAds2xBCM:"
BIBLIOTECA=Cena (BIBLIOTECA)
BRASAO=Elemento (BRASAO, cena=BIBLIOTECA)
JARDIM=Cena (JARDIM, BIBLIOTECA)
CABECA=Elemento (CABECA, cena=JARDIM)
class Verao ():
    def __init__(self):
        JARDIM.vai()
        
if __name__ == "__main__":
    Verao()