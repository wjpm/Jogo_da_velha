from utilitarios import *

cont_jogadas = 1

titulo('jogo da velha')
player_inicial = sorteio_player()

while True:
    if player_inicial == 1:
        if cont_jogadas % 2 == 1:
            menu()
            if jogadas() == 0:
                break
            exibe_tab()
        else:
            titulo('jogada do computador')
            sleep(1)
            jogada_comp()

    if player_inicial == 2:
        if cont_jogadas % 2 == 1:
            titulo('jogada do computador')
            sleep(1)
            jogada_comp()
        else:
            menu()
            if jogadas() == 0:
                break
            exibe_tab()

    if vitoria() == 1:
        print()
        titulo('fim de jogo')
        if player_inicial == 1:
            if cont_jogadas % 2 == 1:
                print(f'\033[32mO jogador "X" ganhou!!!\033[m\n-> Jogadas {cont_jogadas} rodadas.')
            else:
                print(f'\033[32mO jogador "O" ganhou!!!\033[m\n-> Jogadas {cont_jogadas} rodadas.')
            exibe_tab()
            linha()
            break

        if player_inicial == 2:
            if cont_jogadas % 2 == 1:
                print(f'\033[32mO jogador "O" ganhou!!!\033[m\n-> Jogadas {cont_jogadas} rodadas.')
            else:
                print(f'\033[32mO jogador "X" ganhou!!!\033[m\n-> Jogadas {cont_jogadas} rodadas.')
            exibe_tab()
            linha()
            break

    if cont_jogadas == 9:
        titulo('## Empate. Deu velha! ##')
        exibe_tab()
        break
    cont_jogadas += 1
