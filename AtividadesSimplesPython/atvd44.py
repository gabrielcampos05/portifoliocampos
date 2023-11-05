#Gabriel Campos Amaral Ribeiro
#15/05/2023

#Desafio 50

s=0

for x in range(0,6):
    g=int(input('Digite um numero:'))
    if (g%2==0):
        s+=g

print(f'A soma de todos os numeros pares é {s}')
