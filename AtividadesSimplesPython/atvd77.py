#Gabriel Campos Amaral Ribeiro
#27/05/2023

num=str(input('Digite:'))

abertos=num.count('(')
fechados=num.count(')')
total=abertos+fechados

if fechados == abertos:
 print('Está certo')
else:
 print('Está errado')


