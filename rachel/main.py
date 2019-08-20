from browser import document, html
URL='http://lorempixel.com/300/city/5'
pydom=document['pydiv']
pydom.html=''
pydom.html='Hello World'
div1=html.div()
pydom<=div1
imagem1=html.img(src=URL, width=300, height='300px')
div1<=imagem1