#Gabriel Campos Amaral Ribeiro
#27/05/2023

teste=[]
teste.append('Gabriel')
teste.append(17)

galera=[]
galera.append(teste[:])
teste[0] ='João'
teste[1] = 12
galera.append(teste[:])
#print(galera)

geral=[['Gabriel',17], ['João',12], ['Roberta',51], ['Eduardo',52]]
#print(geral[0][0])

for p in galera:
    print(p[0])

glr=[]
dado=[]

for x in range(0,2):
    nome=str(input('Digite seu nome:'))
    dado.append(nome)
    idade=int(input('Digite sua idade:'))
    dado.append(idade)
    #Copia a lista;
    glr.append(dado[:])
    #Clear apaga a lista
    dado.clear()

    for x in glr:
        if x[1]>=18:
            print(f'{x[0]} é maior de idade.')
        else:
            print(f' {x[0]} é menor de idade.')




print(glr)


