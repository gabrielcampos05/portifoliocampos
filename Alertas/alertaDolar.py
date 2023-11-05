#Gabriel Campos Amaral Ribeiro
#Inicio:26/06/2023
#Fim:26/06/2023

#Programa que gera alertas sobre o dolar
#O programa nao pode ser executado perfeitamente como deveria pois nao vou pagar pelo heroku


#Obtem a informacao que queremos
import requests

#Biblioteca que trata sobre o envio de emails
import win32com.client as win32

site=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
cot=site.json()
cotacao=float(cot['USDBRL']['bid'])

# Inicializa as variáveis com a primeira cotação obtida
maior = cotacao
menor = cotacao

# Compara com a última cotação
if cotacao > maior:
    maior = cotacao
if cotacao < menor:
    menor = cotacao

#Envia um aviso no email
if cotacao<maior:
    #Conecta ao outlook do pc
    outlook = win32.Dispatch('outlook.application')
    #Cria o email
    mail = outlook.CreateItem(0)
    #Para quem vai enviar
    mail.To = '...@gmail.com'
    #Assunto do email
    mail.Subject = 'Dolar caiu !!! '
    mail.HTMLBody=f'''
        <h1>Cotacao do dolar<h1>
        <p>Cotacao antiga={maior}<p>
        <p>Cotacao atual do dolar: {cotacao:.2f} reais<p>

        <p>Att.Bot do dolar<p>
    '''

    mail.Send()

else:
    #Conecta ao outlook do pc
    outlook = win32.Dispatch('outlook.application')
    #Cria o email
    mail = outlook.CreateItem(0)
    #Para quem vai enviar
    mail.To = 'gc694136@gmail.com'
    #Assunto do email
    mail.Subject = 'Dolar aumentou  :(  '
    mail.HTMLBody=f'''
        <h1>Cotacao do dolar<h1>
        <p>Cotacao antiga={menor}<p>
        <p>Cotacao atual do dolar: {cotacao:.2f} reais<p>

        <p>Att.Bot do dolar<p>
    '''

    mail.Send()


print()
print('\033[1;32mEmail enviado com sucesso\033[m')
print()


#Deploy - Heroku 
...
