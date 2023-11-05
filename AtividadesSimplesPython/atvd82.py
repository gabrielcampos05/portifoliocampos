#Gabriel Campos Amaral Ribeiro
#01/06/2023


matriz=[]
linha=3
coluna=3
soma=0
maior=0
somaPar=0

#Cria a matriz
for l in range(linha):
    linha=[]
    for c in range(coluna):
        val=int(input(f'Digite [{l+1}][{c+1}]:'))
        #Soma todos os pares;
        if val%2==0:
            somaPar+=val
        linha.append(val)
    matriz.append(linha)


#Faz a procura pelo valor dentro da faixa desejada:
for val in matriz[1]:
    if val > maior:
        maior=val

#Soma todos os elementos da coluna 3
coluna_desejada=[]
for linha in matriz:
    coluna_desejada.append(linha[2])
    soma+=linha[2]

#Printa toda a matriz
for linha in matriz:
    print(linha)

print(f'A soma de toda a coluna 3 é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')
print(f'A soma de todos os pares é: {somaPar}')

#Seleciona as linhas
#linha_desejada = matriz[2]
#print(linha_desejada)





