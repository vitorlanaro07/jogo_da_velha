#classe velha
import pygame as pg
import numpy as np

class Velha():
    def __init__(self, x, y, imagem, escala):
        width = imagem.get_width()
        height = imagem.get_height()
        self.imagem = pg.transform.scale(imagem,(int(width * escala), int(height * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)
        self.coordenadas_das_jogadas = []

    def incrementa_coordenadas(self, nova_coordenada):
        try:
            self.coordenadas_das_jogadas.index(nova_coordenada)
            return True
        except:
            self.coordenadas_das_jogadas.append(nova_coordenada)
            return False

    def draw_velha(self, surface):
        return surface.blit(self.imagem, (self.rect.x, self.rect.y))

    def get_surface(self):
        return self.imagem
