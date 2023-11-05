#Gabriel Campos Amaral Ribeiro
#25/05/2023

num='zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

escolha=int(input('Numero[0-20]:'))
while escolha<0 or escolha>20:
    escolha = int(input('Numero[0-20]:'))


print(f'\033[1:34m {escolha} = {num[escolha].upper()} \033[m')

