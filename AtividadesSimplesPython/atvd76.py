#Gabriel Campos Amaral Ribeiro
#27/05/2023

lista=[]
listaPar=[]
listaImpar=[]


while True:
    print('Bem vindo ao programa de listas Par e Impar')
#Para só aceitar numeros:
    try:
        num = int(input('Digite um número: '))
    except ValueError:
        print('Você não digitou um número.')
        continue

    lista.append(num)

    continuar=str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]


#Adiciona os pares e impares em cada lista desejada;
    if num%2==0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

#Encerra o programa;
    if continuar == 'N':
        break

#Mostra lista;
print('.'*10)
print(f'Lista completa:{lista.sort()}')
print('.'*10)
print(f'Lista com números pares:{listaPar.sort()}')
print('.'*10)
print(f'Lista com números impares:{listaImpar.sort()}')
print('.'*10)