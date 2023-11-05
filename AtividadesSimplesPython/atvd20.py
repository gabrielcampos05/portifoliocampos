#Gabriel Campos Amaral Ribeiro
#13/05/2023

import random

x=int(input('Digite um numero de [0-5]:'))

#randrange(inicio,fim)
sorteio=random.randrange(0,5)

if x==sorteio:
    print('Parabens!!! Você venceu o jogo')
else:
    print('Vish,você perdeu :( ')

print(f'O numero sorteado foi {sorteio} e você digitou {x}')




