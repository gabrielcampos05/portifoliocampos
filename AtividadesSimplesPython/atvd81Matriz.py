#Gabriel Campos Amaral Ribeiro
#01/06/2023

matriz=[]
linha = []
colunas=3
linhas=3

#Linhas
for l in range(linhas):
    linha=[]
    #Colunas
    for c in range(colunas):
        val=int(input(f'Digite[{l+1}][{c+1}]:'))
        linha.append(val)
    matriz.append(linha)

for linha in matriz:
    print(linha)

