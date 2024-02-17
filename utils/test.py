import unittest
import code


class TestValidarEntrada(unittest.TestCase):

  def test_valor_valido(self):
    valor = "5"
    resultado = code.validar_entrada(valor)
    self.assertTrue(resultado)

  def test_valor_invalido_fuera_rango(self):
    valor = "11"
    resultado = code.validar_entrada(valor)
    self.assertFalse(resultado)

  def test_valor_invalido_no_numerico(self):
    valor = "a"
    resultado = code.validar_entrada(valor)
    self.assertFalse(resultado)


class TestCalcularPromedio(unittest.TestCase):

  def test_lista_vacia(self):
    numeros = []
    resultado = code.calcular_promedio(numeros)
    self.assertEqual(resultado, None)

  def test_lista_con_un_numero(self):
    numeros = [5]
    resultado = code.calcular_promedio(numeros)
    self.assertEqual(resultado, 5)

  def test_lista_con_varios_numeros(self):
    numeros = [1, 2, 3, 4, 5]
    resultado = code.calcular_promedio(numeros)
    self.assertEqual(resultado, 3)

if __name__ == "__main__":
  unittest.main()