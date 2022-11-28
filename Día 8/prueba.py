import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    # FUNCIÓN DE PRUEBA
    # que empiece por test
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "Buen Dia")


# PARA PROTEGER CÓDIGO REFERENCIA A CLASE MAIN
# EN PYTHON MAIN NO SE USA COMO EN OTROS IDIOMAS
if __name__ == '__main__':
    unittest.main()
