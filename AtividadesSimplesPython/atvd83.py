#Gabriel Campos Amaral Ribeiro
#01/06/2023

sorteio=[]

import random
import time
cont=0
jogos=int(input('Quantos jogos você deseja?:'))

for x in range(jogos):
    for y in range(6):
        num=random.randint(1,60)
        cont=cont+1

        while num in sorteio:
            num = random.randint(1, 60)
        sorteio.append(num)

        print(f'{num} ', end='')
        time.sleep(0.5)
        if cont==6:
            print()
            cont=0






