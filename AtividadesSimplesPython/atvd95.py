#Gabriel Campos Amaral Ribeiro
#04/06/2023

import time

def estetica():
    print('~'*30)

def contador():
    for x in range(1,11):
        print(f' {x}',end='')
        #time.sleep(0.5)
    print()

def contador2():
    for x in range(10,-1,-2):
        print(f' {x}',end='')
        #time.sleep(0.5)
    print()

def contadorUsuario(inicio,fim,passo):

    if inicio>fim and passo==0:
        print(f'Contagem de {inicio}-{fim} de {passo} em {passo}:')
        for x in range(inicio, fim-1 , -1):
            print(f' {x}', end='')
        print()

    elif inicio<fim and passo==0:
        print(f'Contagem de {inicio}-{fim} de {passo} em {passo}:')
        for x in range(inicio,fim+1,1):
            print(f' {x}', end='')
        print()

    elif inicio > fim:
        print(f'Contagem de {inicio}-{fim} de {passo} em {passo}:')
        if passo<0:
            for x in range(inicio, fim - 1, passo):
                print(f' {x}', end='')
            print()
        else:
            for x in range(inicio, fim - 1, -passo):
                print(f' {x}', end='')
            print()

    elif inicio<fim and passo<0:
            print(f'Contagem de {inicio}-{fim} de {passo} em {passo}:')
            for x in range(inicio,  fim+1, passo*-1):
                print(f' {x}', end='')
            print()

    else:
        print(f'Contagem de {inicio}-{fim} de {passo} em {passo}:')
        for x in range(inicio,fim+1,passo):
            print(f' {x}',end='')
        print()



estetica()
print('Contagem de 1-10 de 1 em 1:')
contador()
estetica()

print('Contagem de 10-0 de 2 em 2:')
contador2()
estetica()


print('Agora é a sua hora de escolher os parametros:')
inicio = int(input('Digite o inicio:'))
fim = int(input('Digite o fim:'))
passo = int(input('Digite o passo:'))
estetica()
contadorUsuario(inicio,fim,passo)
