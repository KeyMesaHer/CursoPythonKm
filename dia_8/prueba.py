import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'Buen dia Keissy'
        resultado = Cambia_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado, 'Buen Dia Keissy')


if __name__ == '__main__':
    unittest.main()
