#Gabriel Campos Amaral Ribeiro
#14/05/2023

#Atividade 40

nota1=float(input('Digite a sua primeira nota:'))
nota2=float(input('Digite a sua segunda nota:'))
media=(nota1+nota2)/2

if media<5.0:
    print('\033[1;31m REPROVADO \033[m')
elif media>=5.0 and media <=6.9:
    print('\033[1;33m RECUPERAÇÃO \033[m')
else:
    print('\033[1;32m APROVADO \033[m')