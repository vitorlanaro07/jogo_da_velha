import pygame as pg
from modulos import botao, velha, jogador

def jogo():
	aplicacao_rodando = True
	menu = "menu"

	janela = inicializa_tela()
	botao_sair, botao_voltar = inicializa_botoes()
	imagem_velha, imagem_cruz, imagem_circulo = inicializa_jogo()
	imagem_espaco = pg.image.load("imagens/titulo.png").convert_alpha()
	janela.blit(imagem_espaco, (140, 260))

	while aplicacao_rodando:
		janela.fill((202, 228, 241))
		if (menu == "menu"):
			janela.blit(imagem_espaco, (140, 260))
			velha_tabuleiro, jogadorX, jogadorO, jogador_o_ganhou, jogador_x_ganhou = inicia_novo_jogo(imagem_velha, imagem_cruz, imagem_circulo)
			if botao_sair.draw(janela):
				aplicacao_rodando = False
		elif (menu == "jogo"):
			velha_tabuleiro.draw_velha(janela)
			realiza_jogada(velha_tabuleiro, jogadorX,jogadorO)
			confere_se_ha_vencedor(velha_tabuleiro,jogador_x_ganhou, jogador_o_ganhou,jogadorX,jogadorO)

			if botao_voltar.draw(janela):
				menu = "menu"

		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					menu = "jogo"
			if event.type == pg.QUIT:
				aplicacao_rodando = False

		pg.display.update()
	pg.quit()


def inicializa_tela():
	tela_largura= 800
	tela_altura = 600
	janela = pg.display.set_mode((tela_largura, tela_altura))
	pg.display.set_caption('Jogo da velha')
	return janela

def inicializa_botoes():
	imagem_botao_sair = pg.image.load('imagens/Sair.png').convert_alpha()
	imagem_botao_voltar = pg.image.load('imagens/Voltar.png').convert_alpha()
	botao_sair = botao.Botao(325, 500, imagem_botao_sair, 1)
	botao_voltar = botao.Botao(681, 540, imagem_botao_voltar, 0.8)
	return botao_sair, botao_voltar

def inicializa_jogo():
	imagem_velha = pg.image.load("imagens/Velha.png").convert_alpha()
	imagem_circulo = pg.image.load("imagens/Circulo.png").convert_alpha()
	imagem_cruz = pg.image.load("imagens/Cruz.png").convert_alpha()
	return imagem_velha, imagem_cruz, imagem_circulo

def get_area(click):

	area00 = (120, 60)
	area01 = (300, 60)
	area02 = (480, 60)
	area10 = (120, 220)
	area11 = (300, 220)
	area12 = (480, 220)
	area20 = (120, 370)
	area21 = (300, 370)
	area22 = (480, 370)

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


def get_vitoria(vitoria_tipo):

	vitoria1 = pg.image.load("imagens/ganhador_diagonal.png").convert_alpha()  # (95,45)
	vitoria2 = pg.image.load("imagens/ganhador_diagonal_oposta.png").convert_alpha()  # (87,45)
	vitoria3 = pg.image.load("imagens/ganhador_vertical.png")  # (87, 105)
	vitoria4 = pg.image.load("imagens/ganhador_vertical.png")  # (87, 265)
	vitoria5 = pg.image.load("imagens/ganhador_vertical.png")  # (87, 415)
	vitoria6 = pg.image.load("imagens/ganhador_horizontal.png")  # (170, 45)
	vitoria7 = pg.image.load("imagens/ganhador_horizontal.png")  # (350, 45)
	vitoria8 = pg.image.load("imagens/ganhador_horizontal.png")  # (530, 45)

	if vitoria_tipo == "vitoria_tipo_1":
		return vitoria1, (95,45)
	elif vitoria_tipo == "vitoria_tipo_2":
		return vitoria2, (87,45)
	elif vitoria_tipo == "vitoria_tipo_3":
		return vitoria3, (87, 105)
	elif vitoria_tipo == "vitoria_tipo_4":
		return vitoria4, (87, 265)
	elif vitoria_tipo == "vitoria_tipo_5":
		return vitoria5, (87, 415)
	elif vitoria_tipo == "vitoria_tipo_6":
		return vitoria6, (170, 45)
	elif vitoria_tipo == "vitoria_tipo_7":
		return vitoria7, (350, 45)
	elif vitoria_tipo == "vitoria_tipo_8":
		return vitoria8, (530, 45)


def inicia_novo_jogo(imagem_velha, imagem_cruz, imagem_circulo):
	#carrega imagem "pressione espaço"


	#inicializa tabuleiro e jogadores
	velha_tabuleiro = velha.Velha(50, 0, imagem_velha, 0.9)
	jogadorX = jogador.Jogador(imagem_cruz, True)
	jogadorO = jogador.Jogador(imagem_circulo, False)

	#estado de ganhador inicia nulo
	jogador_x_ganhou = None
	jogador_o_ganhou = None

	return velha_tabuleiro, jogadorX, jogadorO, jogador_o_ganhou, jogador_x_ganhou


def realiza_jogada(velha_tabuleiro, jogadorX,jogadorO):
	if bool(get_area(pg.mouse.get_pos())) and pg.mouse.get_pressed()[0] == 1:  # Se onde o mouse estiver for um local valido e ainda houver click
		coordenadas = get_area(pg.mouse.get_pos())
		existe = velha_tabuleiro.incrementa_coordenadas(
			coordenadas)  # preciso conferir as coordenadas já existentes na velha, se não existir eu incremento, se não, não realiza ação
		if not existe:
			if jogadorX.vez:
				jogadorX.incrementa_coordenadas(coordenadas)
				print("X", jogadorX.get_coordenadas())
				jogadorX.vez = False
				jogadorO.vez = True
				velha_tabuleiro.get_surface().blit(jogadorX.get_surface(), coordenadas)
			else:
				jogadorO.incrementa_coordenadas(coordenadas)
				print("O", jogadorO.get_coordenadas())
				jogadorO.vez = False
				jogadorX.vez = True
				velha_tabuleiro.get_surface().blit(jogadorO.get_surface(), coordenadas)
		else:
			pass


def confere_se_ha_vencedor(velha_tabuleiro,jogador_x_ganhou,jogador_o_ganhou,jogadorX,jogadorO):
	try:
		jogador_x_ganhou, vitoria_tipo = jogadorX.sera_que_ganhou()
	except:
		pass
	try:
		jogador_o_ganhou, vitoria_tipo = jogadorO.sera_que_ganhou()
	except:
		pass

	if jogador_x_ganhou:
		ganhou, coordenadas = get_vitoria(vitoria_tipo)
		velha_tabuleiro.get_surface().blit(ganhou, coordenadas)
	elif jogador_o_ganhou:
		ganhou, coordenadas = get_vitoria(vitoria_tipo)
		velha_tabuleiro.get_surface().blit(ganhou, coordenadas)


if (__name__ == "__main__"):
	jogo()
