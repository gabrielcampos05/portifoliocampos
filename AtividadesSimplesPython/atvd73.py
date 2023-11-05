#Gabriel Campos Amaral Ribeiro
#26/05/2023
maior=0
menor=0
lista=[]

for num in range(5):
    lista.append(int(input('Digite um num:')))

    if num==0:
        maior=lista[num]
        menor=lista[num]
    else:
        if lista[num]>maior:
            maior=lista[num]
        if lista[num]<menor:
            menor=lista[num]

print(lista)




for x,num in enumerate(lista):
    if num==maior:
      print(f'O maior valor é {maior}')
      print(f'O maior valor está na posição:{x+1}')
    print('.' * 10)
    if num==menor:
      print(f'O menor valor é {menor}')
      print(f'O menor valor está na posição {x+1}')