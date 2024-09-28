# tests/test_main.py
import unittest
from main import gerar_comida, largura, altura, tamanho_quadrado

class TestGerarComida(unittest.TestCase):

    def test_gerar_comida(self):
        comida_x, comida_y = gerar_comida()
        # Verifica se a comida está dentro dos limites da tela
        self.assertGreaterEqual(comida_x, 0)
        self.assertLess(comida_x, largura)
        self.assertGreaterEqual(comida_y, 0)
        self.assertLess(comida_y, altura)

    def test_comida_alinhada(self):
        comida_x, comida_y = gerar_comida()
        # Verifica se a comida está alinhada com o grid
        self.assertEqual(comida_x % tamanho_quadrado, 0)
        self.assertEqual(comida_y % tamanho_quadrado, 0)

if __name__ == '__main__':
    unittest.main()