#Gabriel Campos Amaral Ribeiro
#13/06/2023

def estetica():
    print('~'*60)

#SQL utilizando Python

#Calculos a serem desenvolvidos:
#a)Faturamento por loja
#b)Quantidade de produtos vendidos por loja
#c)Ticket médio
#d)Enviar um email

#Importação da base de dados
#pd é um apelido pro pandas
import pandas as pd


#Lê o arquivo excel
vendas=pd.read_excel('Vendas.xlsx')

#Visualização completa das colunas da base de dados
#pd.set_option(opcao,valor)
#None=nada
pd.set_option('display.max_columns',None)
#print(vendas)


#Faturamento

#Seleciona as colunas
#print(vendas[['ID Loja','Valor Final']])
#Soma a coluna desejada
#vendas.groupby('ID Loja').sum()

#Seleciona as colunas e soma a desejada
print()
print('FATURAMENTO:')
faturamento=vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

#Quantidade de produtos vendidos por loja
estetica()
print('Quantidade de produtos vendido por loja:')
product=vendas[['ID Loja','Quantidade']].groupby("ID Loja").sum()
print(product)

#Ticket médio
#Faturamento/Quantidade de produtos vendidos
#nomeDatabela[Coluna desejada]
estetica()
#().toframe() é para transformar em tabela,pois na operação matematica não forma-se tabela
ticket=(faturamento['Valor Final']/product['Quantidade']).to_frame()
#Mudar nome de uma coluna de uma tabela
ticket=ticket.rename(columns={0:'Ticket Médio'})
print(ticket)

#Envio do relatório por email

#Biblioteca para enviar emails
import win32com.client as win32

#Conecta ao outlook do pc
outlook = win32.Dispatch('outlook.application')
#Cria o email
mail = outlook.CreateItem(0)
#Para quem vai enviar
mail.To = 'gc694136@gmail.com'
#Assunto do email
mail.Subject = 'Relatório de Vendas '
mail.HTMLBody=f'''
<p>Prezados,<p>

<p>Segue o relatório de vendas por cada loja.<p>

<p>Faturamento:<p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}

<p>Quantidade vendida:<p>
{product.to_html()}

<p>Ticket médio dos produtos em cda loja:<p>
{ticket.to_html(formatters={'Ticket Médio':'R${:,.2f}'.format})}

<p>Att.,<p>
<p>Gabriel Campos <p>
'''

mail.Send()
print('\033[1;32mEmail enviado\033[m')


#to_html-Da desing para a tabela


