import random


name1=str(input('Digite o nome da primeira pessoa para participar do sorteio:'))
name2=str(input('Digite o nome da segunda pessoa para participar do sorteio:'))
name3=str(input('Digite o nome da terceira pessoa para participar do sorteio:'))
name4=str(input('Digite o nome da quarta pessoa para participar do sorteio:'))

lista=[name1,name2,name3,name4]

#Embaralha a lista [shuffle]
random.shuffle(lista)

print(lista)

