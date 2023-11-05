#Gabriel Campos Amaral Ribeiro
#14/05/2023

a=int(input('Digite um numero:'))
b=int(input('Digite um outro numero:'))


if a>b:
    print('O\033[1;35m primero valor é o maior \033[m')
elif a<b:
    print('O\033[1;36m segundo valor é o maior \033[m')
else:
    print('\033[1;31m São iguais \033[m')