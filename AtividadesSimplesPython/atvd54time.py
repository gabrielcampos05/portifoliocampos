#Gabriel Campos Amaral Ribeiro
#20/05/2023

import time
escolha=1
tentativas=0
cont=1

n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))

while escolha != 5:
    print('='*20)
    escolha=int(input(f'Faça a sua escolha:\n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n Digite:'))
    print('=' * 20)

    if escolha == 1:
          print(f'{n1} + {n2} = {n1+n2}')
    elif escolha == 2:
          print(f'{n1} * {n2} = {n1 * n2}')
    elif escolha == 3:
          if n1>n2:
                print(f'{n1} > {n2}')
          else:
                print(f'{n2} > {n1}')
    elif escolha== 4:
          n1 = int(input('Digite um número:'))
          n2 = int(input('Digite outro número:'))
    else:
          print('Encerrado')






