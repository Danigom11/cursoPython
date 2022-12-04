import bs4
import requests

# crear una url sin número de página
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

'''# averiguar la clase que queremos extraer
resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

# contiene todos los libros
libros = sopa.select('.product_pod')
# si espacio vacío en el nombre sustituir por un punto
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)
'''

# lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar páginas
for pagina in range(1, 51):

    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # guardar título en una variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver los libros con 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
