#Gabriel Campos Amaral Ribeiro
#02/06/2023

dicionario={}

dicionario['nome']=str(input('Digite o nome:')).capitalize().strip()
dicionario['media']=float(input('Digite a média:'))

if dicionario['media']>= 7.0:
    dicionario['situação']='Aprovado'
else:
    dicionario['situação']='Reprovado'

print(f'Nome: {dicionario["nome"]}')
print(f'Média: {dicionario["media"]}')
print(f'Situação: {dicionario["situação"]}')


