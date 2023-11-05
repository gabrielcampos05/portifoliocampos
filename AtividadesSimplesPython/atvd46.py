#Gabriel Campos Amaral Ribeiro
#16/05/2023


for x in range(1):
    n = int(input('Digite um numero:'))
    if n==2:
     print(f'{n} é primo')
    elif n%n==0 and n%1==0 and n%2==1:
     print(f'{n} é primo')
    else:
     print(f'{n} não é primo')