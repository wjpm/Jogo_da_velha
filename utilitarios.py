from random import randint
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
    player = randint(1, 2)
    # print(player)
    if player == 1:
        print('Computador: Você começa.')
    else:
        print('Computador: Eu começo.')


def exibe_tab():
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{tab[l][c]:^5}]', end='')
        print()


def menu():
    titulo('menu')
    tab_jogadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for l in range(3):
        for c in range(3):
            print(f'[{tab_jogadas[l][c]:^5}]', end='')
        print()
    print()


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
        print('Posição ocupada')
    tab[posicoes[jogador-1][0]][posicoes[jogador-1][1]] = 'X'
    exibe_tab()


