#Gabriel Campos Amaral Ribeiro
#10/06/2023


def leiaInt(num):

    while True:
        try:

            val = input(num)
            return val

        except Exception:
            print('\033[1;31m VALOR INVALIDO \033[m')

        except KeyboardInterrupt:
            print('\n O usuário pulou a digitação do numero')
            val=0
            return val


def leiaFloat(num):

    while True:
        try:

            val=input(num)
            return val

        except Exception:
            print('\033[1;31m VALOR INVALIDO \033[m')

        except KeyboardInterrupt:
            print('\n O usuário pulou a digitação do numero')
            val=0
            return val


#Programa principal

inteiro=leiaInt('Digite um numero: ')
real=leiaFloat('Digite um numero:')

print(f'O número inteiro que você digitou foi: {inteiro} e o numero real foi:{real}')










