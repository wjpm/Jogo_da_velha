from utilitarios import *

cont_jogadas = 1

# titulo('jogo da velha')
while True:
    menu()
    player01 = int(input(f'Escolha uma posição de 1 a 9 para fazer sua jogada\nou 0 para encerrar: '))
    # print('\n' * 30)
    if player01 == 0:
        titulo('jogo encerrado !')
        break
    if cont_jogadas == 9:
        titulo('Empate. Deu velha !')
        break
    cont_jogadas += 1
    # print(cont_jogadas)
    jogadas(player01)
    clear()


