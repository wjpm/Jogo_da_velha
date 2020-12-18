from random import randint
from time import sleep
tab = [['', '', ''], ['', '', ''], ['', '', '']]


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
    if tab[posicoes[jogador-1][0]][posicoes[jogador-1][1]] != '':
        print('Posição ocupada, jogue novamente')
    tab[posicoes[jogador-1][0]][posicoes[jogador-1][1]] = 'X'


def jogada_comp():
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
    # print(f'primeira:{jogadaPC}')
    while tab[posicoes[jogadaPC-1][0]][posicoes[jogadaPC-1][1]] != '':
        jogadaPC = randint(1, 9)
        # print(f'segunda:{jogadaPC}')
    tab[posicoes[jogadaPC-1][0]][posicoes[jogadaPC-1][1]] = 'O'
    exibe_tab()


