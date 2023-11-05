#Gabriel Campos Amaral Ribeiro
#26/05/2023

lista=[]

while True:

        num = (int(input('Digite um numero:')))

        if num not in lista:
            lista.append(num)
        else:
            print('Numero duplicado! Sem adição')

        continuar = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
        if continuar == 'N':
            #Coloca em ordem
            lista.sort()
            print(lista)
            break