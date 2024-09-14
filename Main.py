#Configurações iniciais - é necessário instalar o Pygame.
import random
from fastapi import FastAPI
import pygame

app = FastAPI()

#Iniciando o Pygame.

pygame.init()

#Criando a tela.

pygame.display.set_caption("Jogo Snake Python")

largura, altura = 1200, 800

tela = pygame.display.set_mode((largura, altura))

relógio = pygame.time.Clock()

#Definindo as cores

preta = (0, 0, 0)

branca = (255, 255, 255)

vermelho = (255, 0, 0)

verde = (0, 255, 0)

#Parâmetros do personagem

tamanho_quadrado = 20

Velocidade_jogo = 15

def gerar_comida():

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):

    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):

    for pixel in pixels:

        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):

    fonte = pygame.font.SysFont("Helvetica", 35)

    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)

    tela.blit(texto, [1, 1])
