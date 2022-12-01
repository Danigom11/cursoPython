import zipfile
import shutil

# Comprimir archivo
'''
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()
'''

# Descomprimir archivo
'''
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()
'''

# Comprimir con shutil
# más práctico y directo
# comprime una carpeta con lo que haya dentro
'''
carpeta_origen = 'C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 9\\mover'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)
'''

# Descomprimir con shutil
shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion Terminada', 'zip')
