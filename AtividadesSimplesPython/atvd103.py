#Gabriel Campos Amaral Ribeiro
#09/06/2023


def leiaInt(num):


    while True:
        try:

            val = int(input(num))
            return val

        except ValueError:
            print('\033[1;31m VALOR INVALIDO \033[m')







inteiro=leiaInt('Digite um numero: ')


print(f'O número inteiro que você digitou foi: {inteiro}')









