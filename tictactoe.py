import numpy as np



def main():
    jogo = cria_jogo()
    x = 0

    jogador1 = input("Informe se jogará com X ou O: ").upper() #Entrada do jogador
    if jogador1 == "X":
        jogador2 = "O"
    else:
        jogador2 ="X"

    vez = jogador1

    while(x < 10):
        linha = int(input("Informe o Valor da linha: "))
        coluna = int(input("Informe o valor da coluna: "))
        if vez == jogador1:
            jogo = incrementa_posicao(jogo, linha, coluna, jogador1)
            soluçoes_diagonais(jogo,jogador1)
            vez = jogador2
        else:
            jogo = incrementa_posicao(jogo, linha, coluna, jogador2)
            soluçoes_diagonais(jogo,jogador2)
            vez = jogador1
        x += 1
        print(jogo)


#Função que inicializa o "Jogo", basicamente ele cria uma matriz com linha e coluna
def cria_jogo():
    jogo = np.array([
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ])
    return jogo

#Função que incrementa posição usando como paramento o jogo, a linha, a coluna e o o jogador de quem é a vez
def incrementa_posicao(jogo,linha,coluna,jogador):
    jogo[linha][coluna] = jogador
    return (jogo)

#Função que verifica se o jogador conseguiu marcar os 3 pontos em linha reta
def soluçoes_diagonais(jogo,jogador):
    if (jogo[0][0] == jogador) and (jogo[1][1] == jogador) and (jogo[2][2] == jogador):
        print("Ok")
    elif (jogo[2][0] == jogador) and (jogo[1][1] == jogador) and (jogo[0][2] == jogador):
        print("Ok")

    elif (jogo[0][0] == jogador) and (jogo[1][0] == jogador) and (jogo[2][0] == jogador):
        print("Ok")
    elif (jogo[0][1] == jogador) and (jogo[1][1] == jogador) and (jogo[1][1] == jogador):
        print("Ok")
    elif (jogo[0][2] == jogador) and (jogo[1][2] == jogador) and (jogo[2][2] == jogador):
        print("Ok")

    elif (jogo[0][0] == jogador) and (jogo[0][1] == jogador) and (jogo[0][2] == jogador):
        print("Ok")
    elif (jogo[1][0] == jogador) and (jogo[1][1] == jogador) and (jogo[1][2] == jogador):
        print("Ok")
    elif (jogo[2][0] == jogador) and (jogo[2][1] == jogador) and (jogo[2][2] == jogador):
        print("Ok")
    else:
        print("No Ok")

if __name__ == '__main__':
    main()