import pygame
import unittest

from Main import gerar_comida, selecionar_velocidade, largura, altura, tamanho_quadrado


class TestSnakeGame(unittest.TestCase):

    def test_gerar_comida(self):
        # Testa se a comida é gerada dentro dos limites da tela
        comida_x, comida_y = gerar_comida()
        self.assertGreaterEqual(comida_x, 0)
        self.assertGreaterEqual(comida_y, 0)
        self.assertLess(comida_x, largura)
        self.assertLess(comida_y, altura)

        # Testa se a comida é gerada em múltiplos do tamanho_quadrado
        self.assertEqual(comida_x % tamanho_quadrado, 0)
        self.assertEqual(comida_y % tamanho_quadrado, 0)

    def test_selecionar_velocidade(self):
        # Testa se as velocidades retornadas estão corretas para cada tecla
        velocidade_x, velocidade_y = selecionar_velocidade(pygame.K_DOWN)
        self.assertEqual(velocidade_x, 0)
        self.assertEqual(velocidade_y, tamanho_quadrado)

        velocidade_x, velocidade_y = selecionar_velocidade(pygame.K_UP)
        self.assertEqual(velocidade_x, 0)
        self.assertEqual(velocidade_y, -tamanho_quadrado)

        velocidade_x, velocidade_y = selecionar_velocidade(pygame.K_RIGHT)
        self.assertEqual(velocidade_x, tamanho_quadrado)
        self.assertEqual(velocidade_y, 0)

        velocidade_x, velocidade_y = selecionar_velocidade(pygame.K_LEFT)
        self.assertEqual(velocidade_x, -tamanho_quadrado)
        self.assertEqual(velocidade_y, 0)

if __name__ == '__Main__':
    unittest.main()
