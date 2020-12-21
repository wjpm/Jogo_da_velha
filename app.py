from utilitarios import *

cont_jogadas = 1

titulo('jogo da velha')
# sorteio_player()

while True:
    # print(f'Rodada: {cont_jogadas}')
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
        if cont_jogadas % 2 == 1:
            print('O jogador X ganhou')
        else:
            print('O jogador O ganhou')
        break

    if cont_jogadas == 9:
        titulo('Empate. Deu velha !')
        exibe_tab()
        break
    cont_jogadas += 1


