#Gabriel Campos Amaral Ribeiro
#16/05/2023

#Coloca referencia
maior=0
menor=0

for x in range(1,5+1):
    peso=float(input(f'Digite o peso da pessoa {x}:'))

#Faz a comparação numero 1
    if x==1:
        maior = peso
        menor = peso
    else:
      if peso>maior:
          maior=peso
      if peso<menor:
          menor=peso


print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')



