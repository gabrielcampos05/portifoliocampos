#Gabriel Campos Amaral Ribeiro
#09/06/2023

def escreva():
    frase=f'Sistema de ajuda'
    t=len(frase)
    a=t+2

    print('\033[1;33m~'*a)
    print(f' {frase} ')
    print('~'*a,'\033[m')

def helps(comando):


    print(f'\033[1;34m Manual do comando {comando}:\033[m')

    print('\033[1;42m ')
    help(comando)
    print('\033[m')




while True:
    escreva()
    comando=str(input('Digite o comando que você deseja:'))
    helps(comando)







