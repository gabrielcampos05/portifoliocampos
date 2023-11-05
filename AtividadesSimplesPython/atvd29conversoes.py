#Gabriel Campos Amaral Ribeiro
#14/05/2023

import math

import matplotlib.testing.compare

#Condições Aninhadas

x=int(input('Digite um numero:'))
op=int(input('Digite\033[1;31m 1-para binario\033[1;32m 2-para octal\033[1;33m 3-para hexadecimal \033[m:'))

if op==1:
    print('\033[1;31m Conversão para binário \033[m')

    #A biblioteca [bin] faz a conversão
    b=bin(x)
    #{b[2:] fatia\limita para aparecer apenas os numeros
    print(f'O numero {x} em binario é {b[2:]}')
elif op==2:
    print('\033[1;32m Conversão para octal \033[m')

    #A biblioteca [oct] faz a conversão
    o=oct(x)
    print(f'O numero {x} em octal é {o[2:]}')
elif op==3:
    print('\033[1;31m Conversão para hexadecimal \033[m')

    #A biblioteca [hex] faz a conversão
    h=hex(x)
    print(f'O numero {x} em hexadecimal é {h[2:]}')
else:
    print('Opção invalida')