#Gabriel Campos Amaral Ribeiro
#01/06/2023
listaPar=[]
listaImpar=[]

for x in range(1,7+1):
    num=int(input(f'Digite o {x}º numero:'))
    if num%2==0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

listaImpar.sort()
listaPar.sort()

print(f'A lista de \033[1;32m números impares \033[m é:{listaImpar}')
print(f'A lista de \033[1;32m números pares \033[m é:{listaPar}')
