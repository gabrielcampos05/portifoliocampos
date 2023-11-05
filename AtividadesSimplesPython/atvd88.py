#Gabriel Campos Amaral Ribeiro
#03/06/2023


trabalho={}
ano_atual=2023
minimo_contribuicao=35

trabalho['Nome']=str(input('Digite o nome:')).capitalize().strip()

ano_nascimento=int(input('Digite seu ano de nascimento:'))
trabalho['Idade']=ano_atual-ano_nascimento

trabalho['CTPS']=int(input('Digite seu CTPS:'))
if trabalho['CTPS']!=0:
    ano_contratacao=int(input('Em que ano você foi contratado?:'))
    trabalho['Tempo de trabalho']=ano_atual-ano_contratacao
    trabalho['Salario']=float(input('Qual o seu salario?:'))
    trabalho['Aposentadoria']=(minimo_contribuicao- trabalho['Tempo de trabalho'])+trabalho['Idade']

    trabalho['Ano de aposentadoria']=ano_contratacao+minimo_contribuicao

    trabalho['Tempo restante de trabalho']=trabalho['Aposentadoria']-trabalho['Idade']

    if trabalho['Tempo restante de trabalho']<=0:
        trabalho['Tempo em anos que ja vai estar aposentado']=trabalho["Tempo restante de trabalho"]*-1
        del trabalho['Tempo restante de trabalho']


print('='*30)
for c,v in trabalho.items():
    print(f'{c}:{v} ')



