#Gabriel Campos Amaral Ribeiro
#27/05/2023

lista=[]

while True:
    try:
     num=int(input('Digite um numero:'))
     lista.append(num)
    except ValueError:
        print('\033[1;31mDigite um inteiro!\033[m')
        continue


    continuar=str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]:')).strip().upper()[0]

    if continuar=='N':
        print('.' * 30)
        print(lista)
        print('.' * 30)
        print(f'A quantidade de numeros digitados foi:{len(lista)}')
        print('.'*30)

#Verifica se determinado numero se encontra na lista
        if 5 in lista:
            print(f'O 5 se encontra na lista')
            print('.' * 30)
#Mostra a posição do numero
            for x,y in enumerate(lista):
             if y==5:
                 print(f'O 5 está na posição {x+1}')
                 print('.' * 30)
        else:
         print('O numero não se encontra na lista')
         print('.' * 30)

        lista.sort(reverse=True)
        print(f'Os valores em forma decrescente é:{lista}')
        print('.' * 30)

        break







#Coloca a lista em ordem
#lista.sort()
#print(lista)
