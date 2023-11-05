#Gabriel Campos Amaral Ribeiro
#30/06/2023

'''                                                                   --- DESAFIO ---
Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que >cancelam< seus cartões tem aumentado significativamente, 
causando prejuízos enormes para a empresa.
O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?
Identificar os principais motivos dos clientes estarem cancelando a assinatura
'''

import pandas as pd
import plotly.express as px

#Arquivo csv

#Cria a tabela vazia
tab_total=pd.DataFrame()

# Caminho para o arquivo CSV
caminho_arquivo = 'projetosPython\Pandas\ClientesBanco.csv'

# Lê o arquivo CSV e cria um DataFrame
tabela = pd.read_csv(caminho_arquivo, encoding='latin1')
tabela=tabela.drop('CLIENTNUM',axis=1)
#Drop=Exclui coluna ou linha 
#AXIS=0-Linha 1-Coluna

#Exibir as primeiras linhas da tabela:
#print(tabela)

#Exclui todas as linhas que possui ao menos um valor vazio
#tabela=tabela.dropna()

#Pega as informacoes da tabela,uma visao geral
#print(tabela.info())

#Descricao geral da tabela
#print(tabela.describe().round(2))



#Exibe a quantidade de clientes x cancelados e numeros
cat=tabela["Categoria"].value_counts()
print(cat)

#Exibe a qauntidade de clinetes x cancelados em percentual
cat_per=tabela["Categoria"].value_counts(normalize=True).round(2)
#print(cat_per)

#Comparacao de clientes x cancelados em forma de grafico

grafico=px.histogram(tabela,x='Meses como Cliente',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Categoria Cartão',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Limite',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Faixa Salarial Anual',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Produtos Contratados',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Taxa de Utilização Cartão',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Qtde Transacoes 12m',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Valor Transacoes 12m',color='Categoria')
grafico.show()

grafico=px.histogram(tabela,x='Contatos 12m',color='Categoria')
grafico.show()









    




