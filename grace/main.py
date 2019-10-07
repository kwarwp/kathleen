# kathleen.grace.main.py
From_spy.Vittolino.Main import Cena,Elemento
From_spy.Vittolino.Main import Inventario as inv
BRASAO="https://www.google.com/search?q=logo+do+bras%C3%A3o+da+biblioteca+da+fiocruz+rj&rlz=1C1EKKP_enBR777BR790&sxsrf=ACYBGNQRC484CK31caMpVhXw_Us1OwMNQw:1569244371251&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimr8HqgufkAhUQF7kGHUxuA3sQ_AUIEigB&biw=1366&bih=657#imgrc=rTN3Q9NzE4cbhM
BIBLIOTECA="https://www.google.com/search?q=logo+do+bras%C3%A3o+da+biblioteca+da+fiocruz+rj&rlz=1C1EKKP_enBR777BR790&sxsrf=ACYBGNQRC484CK31caMpVhXw_Us1OwMNQw:1569244371251&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimr8HqgufkAhUQF7kGHUxuA3sQ_AUIEigB&biw=1366&bih=657#imgrc=rTN3Q9NzE4cbhM
QUEBRACABECA="https://www.google.com/search?rlz=1C1EKKP_enBR777BR790&biw=1366&bih=657&tbm=isch&sxsrf=ACYBGNQL_gc2m1sliSe-WeZg9KldwWGqhA%3A1569244455975&sa=1&ei=J8WIXfqRO5-d5OUPlOKksAU&q=quebra+cabe%C3%A7a+de+dna&oq=quebra+cabe%C3%A7a+&gs_l=img.3.0.35i39j0l9.192965.197693..199334...1.0..3.266.3049.10j15j2......0....1..gws-wiz-img.....10..35i362i39.eskYf_J90jY#imgrc=_nhn-rWAE6c-pM
JARDIM="https://www.google.com/search?rlz=1C1EKKP_enBR777BR790&biw=1366&bih=657&tbm=isch&sxsrf=ACYBGNQP-v3hSW6dfGEtHN_xZBfI5_OeQg%3A1569244656285&sa=1&ei=8MWIXaKFEd_C5OUP5cyX4AU&q=jardim+na+biblioteca+fiocruz&oq=jar&gs_l=img.3.0.35i39j0i67l2j0l7.64589.66641..68493...1.0..4.151.2121.11j9......0....1..gws-wiz-img.....10..35i362i39.sr6rDG7EXrY#imgrc=VpfF7GAds2xBCM
class Primavera():
brasao=Elemento(img=BRASAO)
biblioteca=Cena(img=BIBLIOTECA)
cabeca=Elemento(img=QUEBRACABECA)
jardim=Cena(img=JARDIM)
BRASAO.entra(biblioteca)
Primavera()