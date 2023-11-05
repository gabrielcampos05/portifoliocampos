#Gabriel Campos Amaral Ribeiro
#21/05/2023

import random

sorteio=random.randrange(0,10)
vezes=0
while True:
    esc=str(input('Você quer Par ou Impar?[P/I]:')).upper().strip()[0]
    n=int(input('Digite um valor:'))

    s=sorteio+n
    if (s%2==0):
        if esc=='P':
            print('=' * 20)
            print('\033[1;32mVocê venceu!!!\033[m')
            print('=' * 20)
        else:
            print('=' * 20)
            print('\033[1;31mVocê perdeu!!!\033[m')
            print('=' * 20)
            break
    if (s%2==1):
        if esc == 'I':
            print('=' * 20)
            print('\033[1;32mVocê venceu!!!\033[m')
            print('=' * 20)
        else:
            print('=' * 20)
            print('\033[1;31mVocê perdeu!!!\033[m')
            print('='*20)
            break

    vezes+=1
    print(f'O computador escolheu {sorteio} e você {n},ao total \033[1;34m{s}\033[m')
    print(''*20)


print(f'O computador escolheu {sorteio} e você {n},ao total \033[1;34m{s}\033[m')
print(f'\033[1;32mVocê teve {vezes} vitórias\033[m')
