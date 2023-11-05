#Gabriel Campos Amaral Ribeiro
#25/05/2023
count=0
tupla=int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:'))

print(tupla)

#Conta as vezes que aparece
cont=tupla.count(9)
print(f'O número 9 apareceu:{cont} veze(s)')


if 3 in tupla:
    print(f'O primeiro numero 3 foi digitado na posição:{tupla.index(3)+1}')
else:
    print('A tupla não tem o numero 3')

#Analisa cada elemento da tupla
for n in tupla:
    if n%2==0:
        count=count+1

print(f'Foram digitados {count} numeros pares. ')
