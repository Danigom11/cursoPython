import bs4
import requests
import html.parser


# BÚSQUEDA
resultado = requests.get('https://www.escueladirecta.com/p/trucos-y-atajos-de-excel')

# request.text convierte búsqueda en un string
sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

# busca y ordena en forma de lista los resultados
'''print(sopa.select('title'))
print(len(sopa.select('p')))
print(sopa.select('p')[0])
print(sopa.select('p')[0].getText())'''

# buscar en una class con punto
'''columna_lateral = sopa.select('.container p')
for p in columna_lateral:
    # gettext() quita las etiquetas y deja solo el texto limpio
    print(p.getText())'''

# descargar imágenes
imagenes = sopa.select('.img-responsive')[0]['src']
print(imagenes)
# genera la imagen en binario
imagen_curso_1 = requests.get(imagenes)
# wb es escribir binario
f = open('mi_iagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()



