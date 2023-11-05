#Gabriel Campos Amaral Ribeiro
#14/05/2023

n=int(input('Digite o ano de seu nascimento:'))

x=2023-n
y=18-x

if x<18:
    print(f'Você tem \033[1;32m {x} anos\033[m em 2023 \033[1;32me ainda não precisa se alistar !!!\033[m')
    print(f'Seu alistamento será daqui \033[1;32m {y} ano(s)\033[m')

elif x==18:
    print(f'Você completara \033[1;33m{x} \033[manos em 2023 e \033[1;33mjá é hora de se alistar !!!\033[m')
else:
    print(f'Você tem \033[1;31m{x} \033[manos em 2023 e \033[1;31mjá passou da hora de se alistar !!!\033[m')
    print(f'Caso não tenha feito o alistamento,\033[1;31m está atrasado {y*(-1)} ano(s) \033[m')