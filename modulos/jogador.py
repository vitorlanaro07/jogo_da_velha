import pygame as pg

area00 = (120, 60)
area01 = (300, 60)
area02 = (480, 60)
area10 = (120, 220)
area11 = (300, 220)
area12 = (480, 220)
area20 = (120, 370)
area21 = (300, 370)
area22 = (480, 370)

class Jogador():
    def __init__(self, imagem, vez):
        width = imagem.get_width()
        height = imagem.get_height()
        self.imagem = pg.transform.scale(imagem, (int(width * 0.85), int(height * 0.85)))
        self.coordenadas = []
        self.vez = vez

    # def sera_que_ganhou(self):

    def sera_que_ganhou(self):
        try:
            if bool(self.coordenadas.index(area00) + 1) and bool(self.coordenadas.index(area11) + 1) and bool(self.coordenadas.index(area22) + 1):
                return True, "vitoria_tipo_1"
        except:
            pass


        try:
            if bool(self.coordenadas.index(area02) + 1) and bool(self.coordenadas.index(area11) + 1) and bool(self.coordenadas.index(area20) + 1):
                return True, "vitoria_tipo_2"
        except:
            pass

        try:
            if bool(self.coordenadas.index(area00) + 1) and bool(self.coordenadas.index(area01) + 1) and bool(self.coordenadas.index(area02) + 1):
                return True, "vitoria_tipo_3"
        except:
            pass

        try:
            if bool(self.coordenadas.index(area10) + 1) and bool(self.coordenadas.index(area11) + 1) and bool(self.coordenadas.index(area12) + 1):
                return True, "vitoria_tipo_4"
        except:
            pass

        try:
            if bool(self.coordenadas.index(area20) + 1) and bool(self.coordenadas.index(area21) + 1) and bool(self.coordenadas.index(area22) + 1):
                return True, "vitoria_tipo_5"
        except:
            pass

        try:
            if bool(self.coordenadas.index(area00) + 1) and bool(self.coordenadas.index(area10) + 1) and bool(self.coordenadas.index(area20) + 1):
                return True, "vitoria_tipo_6"
        except:
            pass

        try:
            if bool(self.coordenadas.index(area01) + 1) and bool(self.coordenadas.index(area11) + 1) and bool(self.coordenadas.index(area21) + 1):
                return True, "vitoria_tipo_7"
        except:
            pass

        try:
            if bool(self.coordenadas.index(area02) + 1) and bool(self.coordenadas.index(area12) + 1) and bool(self.coordenadas.index(area22) + 1):
                return True, "vitoria_tipo_8"
        except:
            pass




    def incrementa_coordenadas(self, nova_coordenada):
        try:
            self.coordenadas.index(nova_coordenada)
        except:
            self.coordenadas.append(nova_coordenada)

    def draw(self, surface, coordenadas):
        surface.blit(self.imagem, (coordenadas[0], coordenadas[1]))

    def get_surface(self):
        return self.imagem

    def get_coordenadas(self):
        return self.coordenadas

    def get_id(self):
        return self.identificador



