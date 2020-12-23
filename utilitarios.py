from random import randint
from time import sleep

tab = [['', '', ''], ['', '', ''], ['', '', '']]
tab_pts = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def linha():
    print('=' * 24)


def titulo(texto):
    linha()
    print(f'{texto}'.upper().center(24))
    linha()


def sorteio_player():
    titulo('Vamos ver quem começa')
    print('Sorteando', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.')
    sleep(0.4)
    player = randint(1, 2)
    if player == 1:
        print('Você começa.')
    else:
        print('Computador começa.')
    linha()
    return player


def exibe_tab():
    print('Tabuleiro'.center(21))
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{tab[l][c]:^5}]', end='')
        print()


def menu():
    print('COMO JOGAR'.center(24))
    print('Escolha uma posição de 1 \n'
          'a 9 para fazer sua jogada\n'
          'ou 0 (zero) para encerrar')
    titulo('faça sua jogada')
    print('Posições'.center(21))
    tab_jogadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for l in range(3):
        for c in range(3):
            print(f'[{tab_jogadas[l][c]:^5}]', end='')
        print()
    print()
    exibe_tab()


def jogadas():
    posicoes = [
        None,
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

    try:
        jogador = int(input(f'Sua jogada: '))
        if jogador == 0:
            titulo('jogo encerrado !')
            return 0
        while tab[posicoes[jogador][0]][posicoes[jogador][1]] != '':
            print('\033[31mPosição ocupada, jogue novamente: \033[m', end='')
            jogador = int(input())
            if tab[posicoes[jogador][0]][posicoes[jogador][1]] == '':
                tab_pts[posicoes[jogador][0]][posicoes[jogador][1]] = 1
                break
        tab[posicoes[jogador][0]][posicoes[jogador][1]] = 'X'
        tab_pts[posicoes[jogador][0]][posicoes[jogador][1]] = 1
    except (ValueError, IndexError) as err:
        linha()
        print('\033[31mVALOR INVALIDO.\nRecomece o jogo e observe\nas instruções.\033[m')
        linha()
        return 0


def jogada_comp():
    if verifica_posicao():
        pass
    else:
        posicoes = [
            None,
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
        while tab[posicoes[jogadaPC][0]][posicoes[jogadaPC][1]] != '':
            jogadaPC = randint(1, 9)
        tab[posicoes[jogadaPC][0]][posicoes[jogadaPC][1]] = 'O'
        tab_pts[posicoes[jogadaPC][0]][posicoes[jogadaPC][1]] = -1
        exibe_tab()


def verifica_posicao():
    # Defesa linha
    for l in range(3):
        soma_linha = tab_pts[l][0] + tab_pts[l][1] + tab_pts[l][2]
        if soma_linha == 2:
            linha_perigo = l
            for i in tab_pts:
                p1 = tab_pts.index(i)
                for j in i:
                    p2 = tab_pts[p1].index(j)
                    if soma_linha == 2:
                        defesa_l = tab_pts[linha_perigo][p2] == 0
                        if defesa_l:
                            tab[linha_perigo][p2] = 'O'
                            tab_pts[linha_perigo][p2] = -1
                            return defesa_l
    for c in range(3):
        soma_coluna = tab_pts[0][c] + tab_pts[1][c] + tab_pts[2][c]
        if soma_coluna == 2:
            coluna_perigo = c
            for i in tab_pts:
                p1 = tab_pts.index(i)
                for j in i:
                    p2 = tab_pts[p1].index(j)
                    if soma_coluna == 2:
                        defesa_c = tab_pts[p2][coluna_perigo] == 0
                        if defesa_c:
                            tab[p2][coluna_perigo] = 'O'
                            tab_pts[p2][coluna_perigo] = -1
                            return defesa_c


def vitoria():  # mensagens de vitoria aqui dentro
    # Verificando linhas
    for l in range(3):
        soma_linha = tab_pts[l][0] + tab_pts[l][1] + tab_pts[l][2]
        if soma_linha == 3 or soma_linha == -3:
            return 1

    # Verifica colunas
    for c in range(3):
        soma_culuna = tab_pts[0][c] + tab_pts[1][c] + tab_pts[2][c]
        if soma_culuna == 3 or soma_culuna == -3:
            return 1

    # Verifica diagonais
    soma_diag1 = tab_pts[0][0] + tab_pts[1][1] + tab_pts[2][2]
    soma_diag2 = tab_pts[0][2] + tab_pts[1][1] + tab_pts[2][0]
    if soma_diag1 == 3 or soma_diag1 == -3 or soma_diag2 == 3 or soma_diag2 == -3:
        return 1
    return 0


def jogada_comp_velho():
    posicoes = [
        None,
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
    while tab[posicoes[jogadaPC][0]][posicoes[jogadaPC][1]] != '':
        jogadaPC = randint(1, 9)
    tab[posicoes[jogadaPC][0]][posicoes[jogadaPC][1]] = 'O'
    tab_pts[posicoes[jogadaPC][0]][posicoes[jogadaPC][1]] = -1
    exibe_tab()
