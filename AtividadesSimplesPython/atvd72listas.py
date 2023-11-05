#Gabriel Campos Amaral Ribeiro
#26/05/2023

#lista.append()-add elementos a lista

#print(dir(tuple))-mostra tds as possibilidades

lanche=['hamburguer','suco','pizza','pudim']
lanche[3]='arroz'
#print(lanche)


#lanche.append()-Adiciona elementos na lista
lanche.append('purê')
#print(lanche)

#Insere algo na lista
#lanche.insert(posicao,item)
lanche.insert(1,'feijao')
#print(lanche)

#del()[]-Exclui valores da lista
del lanche[2]
#print(lanche)
lanche.pop(3)
#print(lanche)
lanche.remove('pizza')
#print(lanche)

#Gera valores aleatorios-tuple(range())
val=tuple(range(1,10))
val2=list(range(1,10))
#print(val)
#print(val2)


#Ordenação de valores-
valores=[8,9,6,4,2,3,1,111]
#Ordena os valores de forma crescente- .sort()
valores.sort()
#print(valores)
#Ordena os valores de forma decrescente- .sort(reverse=True)
valores.sort(reverse=True)
#print(valores)

#Mostra a quantidade de valores-len()
#print(len(valores))


#Remove elementos
if 111 in valores:
    valores.remove(111)
#    print(valores)

#Copia os valores de uma lista para outra
#b=a[:]

val=[]
for a in range(0,5):
    val.append(int(input('Digite:')))
print(val)

for x in val:
    print(x)
print('...')

#Mostra o numero e a sua posição
for y,x in enumerate(val):
    print(y,x)
