#Gabriel Campos Amaral Ribeiro
#15/05/2023

import random

print('\033[1;36m Bem vindo ao jogo,seu objetivo é ganhar do computador \033[m')
x=str(input('Escolha entre [Pedra-Papel-Tesoura]:')).strip()

#Coloca o que for digitado em minusculo
opcao=x.lower()

#Faz o sorteio da palavra pelo computador
y=['pedra','papel','tesoura']
sorteio=random.choice(y)

#Condição usuario ganha
if x=='papel' and sorteio=='pedra':
    print('\033[1;32mVocê venceu !!!!\033[m')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')
elif x=='tesoura' and sorteio=='papel':
    print('\033[1;32mVocê venceu !!!!\033[m')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')
elif x=='pedra' and sorteio=='tesoura':
    print('\033[1;32mVocê venceu !!!!\033[m')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')
#Condição usuario perde
elif sorteio=='papel' and x=='pedra\033[m':
    print('\033[1;31mVocê perdeu !!!!\033[m')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')
elif sorteio=='tesoura' and x=='papel':
    print('\033[1;31mVocê perdeu !!!!\033[m')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')
elif sorteio=='pedra' and x=='tesoura':
    print('\033[1;31mVocê perdeu !!!!\033[m')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')
elif sorteio == x:
    print('\033[1;33mEmpate !!!!')
    print(f'\033[1;47m Você digitou:{x} | Computador escolheu:{sorteio} \033[m')


