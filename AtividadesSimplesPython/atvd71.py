#Gabriel Campos Amaral Ribeiro
#26/05/2023
cont=0
tupla='gabriel','campos','amaral','ribeiro','joao','pedro','eduardo','assis','roberta','caroline'

for qlqr in tupla:
    print(f'\n{qlqr} tem ',end=' ')
    for letra in qlqr:
        if letra in 'aeiou':
         print(letra,end=' ')
