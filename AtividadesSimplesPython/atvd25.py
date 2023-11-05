#Gabriel Campos Amaral Ribeiro
#13/05/2023

num1=int(input('Digite um numero:'))
num2=int(input('Digite um numero:'))
num3=int(input('Digite um numero:'))

if ((num1>num2) & (num1>num3)):
    print(f'O maior numero é {num1}')
elif ((num2>num1) & (num2>num3)):
    print(f'O maior numero é {num2}')
else:
    print(f'O maior numero é {num3}')

#########################################

if ((num1 < num2) & (num1 < num3)):
    print(f'O menor numero é {num1}')
elif ((num2 < num1) & (num2 < num3)):
    print(f'O menor numero é {num2}')
else:
    print(f'O menor numero é {num3}')
