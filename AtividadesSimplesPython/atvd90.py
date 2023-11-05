#Gabriel Campos Amaral Ribeiro
#03/06/2023

dados={}
lista=[]

while True:
    dados['Nome']=str(input('Nome:')).strip().capitalize()

    dados['Sexo']=str(input('Sexo[M/F]:')).upper().strip()[0]

    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input('Sexo[M/F]:')).upper().strip()[0]

    dados['Idade']=int(input('Idade:'))

#Adiciona a lista
    lista.append(dados.copy())

    continuar=str(input("Continuar [S/N]:")).upper()[0]
    while continuar not in 'SN':
        continuar = str(input("Continuar [S/N]:")).upper()[0]

    if continuar=='N':
        break

media=dados["Idade"]/len(lista)
print('='*30)
print(f'A media das idades cadastradas é: {media}')
print('='*30)
print(f'A quantidade de pessoas cadastradas foi: {len(lista)}')
print('='*30)

print('Lista da mulheres cadastradas:')
procura=[]
for dados in lista:
    if dados['Sexo']=='F':
        print(f'{dados["Nome"]}')

print('='*30)
print('Lista de pessoas com idade acima da media:')
procura=[]
for dados in lista:
    if dados['Idade']>media:
        print(f'{dados["Nome"]} | {dados["Idade"]} anos')







