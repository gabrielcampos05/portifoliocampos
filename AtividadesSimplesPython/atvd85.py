#Gabriel Campos Amaral Ribeiro
#02/06/2023


#dados=dict()
#x.values()
#x.keys()
#x.items()

#filme={'titulo':'Star Wars','ano':'1977','diretor':'george'}

#for a,b in filme.items():
#    print(f'{a} é {b}')

peoples={'nome':'','idade':'','sexo':'M'}

#peoples['nome']=str(input('Digite o nome:'))
#peoples['idade']=int(input('Digite a idade:'))
#peoples['peso']=int(input('Digite um peso:'))

#print(f'O {peoples["nome"]} tem {peoples["idade"]} anos')

#print(peoples.values())
#print(peoples.keys())
#print(peoples.items())

####### DICIONÁRIO DENTRO DE LISTAS

lista=[]
estado1={'UF':'Minas Gerais','Sigla':'MG'}

lista.append(estado1)

print(lista[0]['UF'])

###################
estado={}
brasil=[]

for x in range(3):
    estado['UF']=str(input('UF:'))
    estado['Sigla']=str(input('Sigla:'))
    #######Importante
    brasil.append(estado.copy())

for x in brasil:
    for k,v in x.items():
       print(k,v)



