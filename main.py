import time
import pygame as pg
from modulos import botao, velha, jogador
import numpy as np

#Criar janela e nome
tela_largura= 800
tela_altura = 600
janela = pg.display.set_mode((tela_largura, tela_altura))
pg.display.set_caption('Jogo da velha')

#carregar imagens
imagem_botao_sair = pg.image.load('imagens/Sair.png').convert_alpha()
imagem_botao_voltar = pg.image.load('imagens/Voltar.png').convert_alpha()
imagem_velha = pg.image.load("imagens/Velha.png").convert_alpha()
imagem_circulo = pg.image.load("imagens/Circulo.png").convert_alpha()
imagem_cruz = pg.image.load("imagens/Cruz.png").convert_alpha()
imagem_espaco = pg.image.load("imagens/titulo.png").convert_alpha()


#criar intancias
botao_sair = botao.Botao(325, 500, imagem_botao_sair, 1)
botao_voltar = botao.Botao(681, 540, imagem_botao_voltar, 0.8)
velha_tabuleiro = velha.Velha(50, 0, imagem_velha, 0.9)

jogadorX = jogador.Jogador(imagem_cruz, True, "X")
jogadorO = jogador.Jogador(imagem_circulo, False, "O")

area00 = (120, 60)
area01 = (300, 60)
area02 = (480, 60)
area10 = (120, 220)
area11 = (300, 220)
area12 = (480, 220)
area20 = (120, 370)
area21 = (300, 370)
area22 = (480, 370)


def get_area(click):
	if 140 <= click[0] <= 300 and 43 <= click[1] <= 181:
		return area00
	if 320 <= click[0] <= 480 and 43 <= click[1] <= 181:
		return area01
	if 500 <= click[0] <= 660 and 43 <= click[1] <= 181:
		return area02
	if 143 <= click[0] <= 304 and 200 <= click[1] <= 343:
		return area10
	if 320 <= click[0] <= 483 and 200 <= click[1] <= 343:
		return area11
	if 500 <= click[0] <= 660 and 200 <= click[1] <= 347:
		return area12
	if 144 <= click[0] <= 302 and 361 <= click[1] <= 486:
		return area20
	if 320 <= click[0] <= 482 and 361 <= click[1] <= 486:
		return area21
	if 500 <= click[0] <= 652 and 361 <= click[1] <= 486:
		return area22

#Jogo
aplicacao_rodando = True
menu = "menu"
coordenadas = 0



while aplicacao_rodando:
	janela.fill((202, 228, 241))
	# Insere os botoes na tela
	if (menu == "menu"):
		janela.blit(imagem_espaco,(140,260))
		if botao_sair.draw(janela):
			aplicacao_rodando = False
	elif (menu == "jogo"):
		velha_tabuleiro.draw_velha(janela)
		if bool(get_area(pg.mouse.get_pos())) and pg.mouse.get_pressed()[0] == 1: # Se onde o mouse estiver for um local valido e ainda houver click
			time.sleep(0.1)
			coordenadas = get_area(pg.mouse.get_pos())
			time.sleep(0.1)
			# preciso conferir as coordenadas já existentes na velha, se não existir eu incremento, se não, não realiza ação
			existe = velha_tabuleiro.incrementa_coordenadas(coordenadas)
			if not existe:
				if jogadorX.vez:
					jogadorX.incrementa_coordenadas(coordenadas)
					print(jogadorX.get_id(), jogadorX.get_coordenadas())
					jogadorX.vez = False
					jogadorO.vez = True
					velha_tabuleiro.get_surface().blit(jogadorX.get_surface(),coordenadas)
				else:
					jogadorO.incrementa_coordenadas(coordenadas)
					print(jogadorO.get_id(), jogadorO.get_coordenadas())
					jogadorO.vez = False
					jogadorX.vez = True
					velha_tabuleiro.get_surface().blit(jogadorO.get_surface(),coordenadas)
			else:
				pass

			if jogadorX.sera_que_ganhou():
				print("Jogador X ganhou")
			elif jogadorO.sera_que_ganhou():
				print("Jogador O ganhou")

		if botao_voltar.draw(janela):
			menu = "menu"

	#event handler
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_SPACE:
				menu = "jogo"
		if event.type == pg.QUIT:
			rodando = False

	pg.display.update()

pg.quit()




