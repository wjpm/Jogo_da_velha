from utilitarios import *

cont_jogadas = 1

titulo('jogo da velha')
# sorteio_player()

while True:
    if cont_jogadas % 2 == 1:
        menu()
        if jogadas() == 0:
            break
        exibe_tab()

    else:
        titulo('jogada do computador')
        sleep(1)
        jogada_comp()

    if vitoria() == 1:
        titulo('fim de jogo')
        exibe_tab()
        if cont_jogadas % 2 == 1:
            print(f'O jogador "X" ganhou com {cont_jogadas} rodadas.')
        else:
            print(f'O jogador "O" ganhou com {cont_jogadas} rodadas.')
        linha()
        break

    if cont_jogadas == 9:
        titulo('Empate. Deu velha !')
        exibe_tab()
        break
    cont_jogadas += 1


