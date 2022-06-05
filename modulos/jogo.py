#classe velha
import pygame as pg

class Jogador():
    def __init__(self, imagem, vez, id):
        width = imagem.get_width()
        height = imagem.get_height()
        self.imagem = pg.transform.scale(imagem, (int(width * 0.85), int(height * 0.85)))
        self.coordenadas = []
        self.clicou = False
        self.vez = vez
        self.identificador = id

    def draw(self, surface, coordenadas):
        surface.blit(self.imagem, (coordenadas[0], coordenadas[1]))

    def get_surface(self):
        return self.imagem

    def get_coordenadas(self):
        return self.coordenadas

    def get_id(self):
        return self.identificador



class Velha():
    def __init__(self, x, y, imagem, escala):
        width = imagem.get_width()
        height = imagem.get_height()
        self.imagem = pg.transform.scale(imagem,(int(width * escala), int(height * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)

    def draw_velha(self, surface):
        return surface.blit(self.imagem, (self.rect.x, self.rect.y))

    def get_surface(self):
        return self.imagem