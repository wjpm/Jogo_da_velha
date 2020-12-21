from random import randint
from time import sleep
tab = [['', '', ''], ['', '', ''], ['', '', '']]
# player1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# computador = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def clear():
    print('\n' * 100)


def linha():
    print('=' * 24)


def titulo(texto):
    linha()
    print(f'{texto}'.upper().center(24))
    linha()


def sorteio_player():
    titulo('Vamos ver quem começa')
    sleep(1.5)
    player = randint(1, 2)
    # print(player)
    if player == 1:
        print('Você começa.'.center(24))
    else:
        print('Computador começa.'.center(24))
        sleep(1.5)


def exibe_tab():
    print('Tabuleiro'.center(21))
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{tab[l][c]:^5}]', end='')
        print()


def menu():
    titulo('faça sua jogada')
    print('Posições'.center(21))
    tab_jogadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for l in range(3):
        for c in range(3):
            print(f'[{tab_jogadas[l][c]:^5}]', end='')
        print()
    print()
    exibe_tab()


def jogadas(jogador=0):
    posicoes = [
        (0, 0),  # 1
        (0, 1),  # 2
        (0, 2),  # 3
        (1, 0),  # 4
        (1, 1),  # 5
        (1, 2),  # 6
        (2, 0),  # 7
        (2, 1),  # 8
        (2, 2)   # 9
    ]
    while tab[posicoes[jogador-1][0]][posicoes[jogador-1][1]] != '':
        print('Posição ocupada, jogue novamente')  # Revisar este, esta sobre pondo a jogada do adversario
        player01 = int(input(f'Escolha uma posição de 1 a 9 para fazer sua jogada\nou 0 para encerrar: '))
        if tab[posicoes[jogador-1][0]][posicoes[jogador-1][1]] == '':
            break
    tab[posicoes[jogador-1][0]][posicoes[jogador-1][1]] = 'X'
    # player1[posicoes[jogador-1][0]][posicoes[jogador-1][1]] = 1
    # print(player1)


def jogada_comp():  # verificar se o computador esta jogando na posição 9
    posicoes = [
        (0, 0),  # 1
        (0, 1),  # 2
        (0, 2),  # 3
        (1, 0),  # 4
        (1, 1),  # 5
        (1, 2),  # 6
        (2, 0),  # 7
        (2, 1),  # 8
        (2, 2)  # 9
    ]
    jogadaPC = randint(1, 9)
    while tab[posicoes[jogadaPC-1][0]][posicoes[jogadaPC-1][1]] != '':
        jogadaPC = randint(1, 9)
    tab[posicoes[jogadaPC-1][0]][posicoes[jogadaPC-1][1]] = 'O'
    # computador[posicoes[jogadaPC - 1][0]][posicoes[jogadaPC - 1][1]] = jogadaPC
    # print(f'Jogada PC {computador}')
    exibe_tab()


def vitoria():
    p_vitoria = [[1, 2, 3],  # Linhas
                 [4, 5, 6],  # Linhas
                 [7, 8, 9],  # Linhas
                 [1, 4, 7],  # Colunas
                 [2, 5, 8],  # Colunas
                 [3, 6, 9],  # Colunas
                 [1, 5, 9],  # Diagonal
                 [3, 5, 7]]  # Diagonal
    posicoes = [
        (0, 0),  # 1
        (0, 1),  # 2
        (0, 2),  # 3
        (1, 0),  # 4
        (1, 1),  # 5
        (1, 2),  # 6
        (2, 0),  # 7
        (2, 1),  # 8
        (2, 2)  # 9
    ]
    jogador1 = 'X'
    for p in p_vitoria:
        for x in p:
            if tab[posicoes[x][0]][posicoes[x][1]] != jogador1:
                break
            else:
                print(f'o jogador {jogador1} ganhou.')



