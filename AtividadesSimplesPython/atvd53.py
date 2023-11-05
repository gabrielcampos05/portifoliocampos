#Gabriel Campos Amaral Ribeiro
#20/05/2023

import random

#randrange(inicio,fim)
sorteio=random.randrange(0,10)

x=0
tentativas=0
contador=1

while x != sorteio:
    x = int(input('Digite um numero de [0-10]:'))
    tentativas=contador+tentativas

    if x == sorteio:
        print(f'\033[1;32mParabens!!! Você venceu o jogo\033[m')
        print(f'O \033[1;33mnumero sorteado \033[m: {sorteio}')
        print(f'O \033[1;34mnumero que voce digitou \033[m: {x}')
        print(f'O \033[1;35mnumero de tentativas \033[m: {tentativas}')