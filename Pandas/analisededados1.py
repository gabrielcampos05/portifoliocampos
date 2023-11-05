#Gabriel Campos Amaral Ribeiro
#30/06/2023

#Python com banco de dados Pandas
#Varios arquivos jogados na pasta
import os #Permite percorrer,abrir arquivos,facilita a analise de dados
import pandas as pd 

#Biblioteca para enviar emails
import win32com.client as win32
  

#Carrega a lista que queremos
lista_arquivo=os.listdir("projetosPython\dadosPandas\Vendas")

#Cria uma tabela zerada
tab_total=pd.DataFrame()

for listas in lista_arquivo:
    
    #Tratar arquivo
    if "vendas".capitalize() in listas:
        #Importar o arquivo
        tab=pd.read_csv(f"projetosPython\dadosPandas\Vendas\{listas}")
        #Adiciona tabelas a uma nova tabela vazia para juntar todas  
        tab_total=tab_total._append(tab)



#Calcular o produto mais vendido em quantidade
#2x'[]' para fazer uma tabela mais 'bonitinha'
#Agrupa o produto com a quantidade vendida,cria uma tabela somente com os dois dados e apresenta os dados na forma decrescente
print('\033[1;32mProdutos mais vendidos:\033[m')
produto_mais_vendido=tab_total.groupby('Produto')[['Quantidade Vendida']].sum().sort_values(by='Quantidade Vendida',ascending=False)
print(produto_mais_vendido)
print()

#Calcular o produto que mais faturou 
print('\033[1;32mFaturamento de cada produto:\033[m')
tab_total['Faturamento']=tab_total['Quantidade Vendida']*tab_total['Preco Unitario']
produto_que_mais_faturou=tab_total.groupby('Produto')[['Faturamento']].sum().sort_values(by='Faturamento',ascending=False)
print(produto_que_mais_faturou)
print()

#Calcular o a loja que mais vendeu em faturamento - criar um grafico

print('\033[1;32mLojas que mais venderam:\033[m')
loja_que_mais_vendeu=tab_total.groupby('Loja')[['Faturamento']].sum().sort_values(by='Faturamento',ascending=False)
print(loja_que_mais_vendeu)
print()

#Graficos
import plotly.express as px

#Cria o grafico
grafico=px.bar(loja_que_mais_vendeu,x=loja_que_mais_vendeu.index,y='Faturamento')

#Exibe o grafico
grafico.show()

grafico2="projetosPython\dadosPandas\grafico.png"

#Conecta ao outlook do pc
outlook = win32.Dispatch('outlook.application')
#Cria o email
mail = outlook.CreateItem(0)
#Para quem vai enviar
mail.To = 'gc694136@gmail.com'
#Assunto do email
mail.Subject = 'Relatorio sobre as lojas '
mail.HTMLBody=f'''

<p>Prezado(a),segue a filtragem dos dados relacionados as tabelas

<h1>Produtos mais vendidos
{produto_mais_vendido.to_html()}

<h1>Produtos que mais faturaram
{produto_que_mais_faturou.to_html(formatters={'Faturamento':'R${:,.2f}'.format})}

<h1>Loja que mais vendeu
{loja_que_mais_vendeu.to_html(formatters={'Faturamento':'R${:,.2f}'.format})}

<h1>Grafico
{grafico2}



        
'''

mail.Send()
print('\033[1;32mEmail enviado\033[m')



    




