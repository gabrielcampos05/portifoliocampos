#Gabriel Campos amaral RIbeiro
#01/07/2023

#API para consulta de CEP

#Toda API precisa do request

import requests as req
import pandas as pd
#Consultar o CEP e mostra as informacoes
conta=0

print('1-Para consultar os dados do CEP; ')
print('2-Para descobrir seu CEP;')
escolha=int(input('Escolha: '))

if escolha==1:



    cep=input('Digite o CEP que voce deseja pegar informacoes:').replace('-','').replace(' ','').replace('.','')

    for x in cep:
        conta=conta+1

    if conta != 8:
        print('CEP invalido')
    else:
        link=f'https://viacep.com.br/ws/{cep}/json/'

        #Abre o link
        requisicao=req.get(link)



        dados=requisicao.json()

        print(dados)
        print()
elif escolha==2:
    #Pega o endereco e mostra o CEP

    uf=input('Digite a sigla do estado: ').upper()
    cidade=input('Digite o nome da cidade: ').title()
    endereco=input('Digite o endereco: ').title()


    link=f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

    requisicao=req.get(link)

    dados=requisicao.json()

    tabela=pd.DataFrame(dados)
    print(tabela)
else:
    print('Nao corresponde')