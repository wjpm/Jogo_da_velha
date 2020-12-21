from utilitarios import *

cont_jogadas = 1

titulo('jogo da velha')
# sorteio_player()

while True:

    if cont_jogadas % 2 == 1:
        menu()
        player01 = int(input(f'Escolha uma posição de 1 a 9 para fazer sua jogada\nou 0 para encerrar: '))
        if player01 == 0:
            titulo('jogo encerrado !')
            break
        jogadas(player01)
        vitoria()

    else:
        titulo('jogada do computador')
        sleep(1)
        jogada_comp()

    if cont_jogadas == 9:
        exibe_tab()
        titulo('Empate. Deu velha !')
        break
    cont_jogadas += 1

