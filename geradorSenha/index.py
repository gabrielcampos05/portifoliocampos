#Gabriel Campos Amaral Ribeiro
#19/07/2023

#Gerador de senha 

import random
import string


def geradorSenha(senha=8):

    #Biblioteca que armazena os caracteres disponiveis
    letras_options=string.ascii_letters
    numeros_options=string.digits
    pontucao_options=string.punctuation

    options=letras_options+numeros_options+pontucao_options

    senha_user=''
    for x in range(0,senha):
        #A biblioteca choice faz esse sorteio de termos que eu escolho
        digit=random.choice(options)
        senha_user+=digit

    return senha_user

    

print('--Gerador de Senha--')
print('Feito por: Gabriel Campos')
print()
senha_us=int(input('Digite o numero de caracteres que sua senha devera ter: '))

resposta=geradorSenha(senha_us)

print()
print(f'Sua senha: {resposta}')
print()


#Implementar uma interface



