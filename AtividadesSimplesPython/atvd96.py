#Gabriel Campos Amaral Ribeiro
#04/06/2023

import time

print('[1]-Com interação com o usuario \n[2]-Sem interação com o usuario')

esc=int(input('Digite:'))
while esc != 1 and esc != 2:
    esc = int(input('Digite:'))

if esc==1:
    #Com interação com usuario
    listaMaior = []


    def maior(*num):


        a=max(listaMaior)
        print(listaMaior)
        print(f'O maior numero digitado foi:{a}')



    while True:

        num=int(input('Digite um num:'))
        listaMaior.append(num)

        continuar=str(input('Deseja digitar mais números?[S/N]:')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Deseja digitar mais números?[S/N]:')).strip().upper()[0]

        if continuar=='N':
            maior(num)
            time.sleep(0.5)
            break



if esc==2:
    #############################################################################################
    #Sem interação com o usuario
    def maior(*num):
        maior = 0

        for val in num:
            if val==1:
                maior=val
            else:
                if val>maior:
                    maior=val

            print(val, end=' ')
            time.sleep(0.5)
        print(f'\nO maior valor é: {maior}')
        print()

    maior(0,2,3,4)
    maior(8,9,10,11,12,6)
    maior(80,90,80,90,60)

