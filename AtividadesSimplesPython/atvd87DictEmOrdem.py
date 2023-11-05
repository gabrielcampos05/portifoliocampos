#Gabriel Campos Amaral Ribeiro
#02/06/2023

import random
import operator

dicionario={}
ordem={}
maior=0
menor=0


#Faz o sorteio dos numeros
for x in range(4):
    dicionario[f'Jogador {x+1}'] = random.randint(1, 6)

#Pega o maior numero
    if x==1:
        maior=dicionario[f'Jogador {x+1}']
    else:
        if dicionario[f'Jogador {x+1}']>maior:
            maior=dicionario[f'Jogador {x+1}']

#Mostra os resultados:
print('Resultados:')
for a,b in dicionario.items():
    print(f'{a} tirou {b}')

#Mostra em ordem crescente:
print()
print('Os resultados em ordem crescente:')
ordem=sorted(dicionario.items(),key=operator.itemgetter(1),reverse=True)
for c,n in enumerate(ordem):
    print(f'{n[0]} com {n[1]}')

print()
print(f'O maior valor sorteado foi:{maior}')


