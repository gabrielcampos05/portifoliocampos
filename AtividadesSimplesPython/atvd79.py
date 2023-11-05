#Gabriel Campos Amaral Ribeiro
#30/05/2023

lista=[]
lista02=[]
listaGordo=[]
listaMagro=[]

cont=0
maior=0
menor=0

while True:
    nome=str(input('Digite o nome:'))
    lista.append(nome)
    peso=int(input('Digite o peso:'))
    lista.append(peso)

    cont=cont+1


    continuar=str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]

#Conta o maior e menor peso
    if cont == 1:
        maior = lista[1]
        menor = lista[1]
    else:
        if lista[1] > maior:
         maior = lista[1]
        if lista[1] < menor:
         menor = lista[1]

    lista02.append(lista[:])
    lista.clear()

    if continuar=='N':

        print(f'Foram cadastradas {cont} pessoas')

#Associa o peso a pessoa:
        for pessoa in lista02:
            if pessoa[1] == maior:
                print(f'A(s) pessoa(s) mais pesadas possuem {maior}kg e são:{pessoa[0]}')
            if pessoa[1] == menor:
                print(f'A(s) pessoa(s) mais leves possuem {menor}kg e são:{pessoa[0]} ')

        break


