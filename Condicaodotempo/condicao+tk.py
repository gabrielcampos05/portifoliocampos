#Gabriel Campos Amaral Ribeiro
#03/07/2023

#Programa que faca um app simples para a consulta de temperatura em determinada cidade


import customtkinter as ctk 
import tkinter as tk
import datetime as dt 
import requests as rq 

lugar=[]

def conversao(kelvin):
    celsius = kelvin - 273.15
    return celsius

def leituraPrevisao():

    digiteLugar=digite.get()
    #Cria uma segunda janela
    janela2=tk.Toplevel()
    janela2.title(f'Condição {digiteLugar.title()}')
    janela2.geometry('450x50')
    janela2.resizable(width=False, height=False) 
    janela2.configure(bg='#313131') 
    janela.configure(fg='red')

    key='88f9ee706197160c65aff2e93f7c0e19'

    link=f'https://api.openweathermap.org/data/2.5/weather?q={digiteLugar}&appid={key}&lang=pt_br'

    requisicao=rq.get(link)

    try:

        dados=requisicao.json()
        descricao=dados['weather'][0]['description']
        temperatura=dados['main']['temp']

        celsius=conversao(temperatura)
        
        pergunta=tk.Label(janela2,text=f'Condição: {descricao} | Temperatura em {digiteLugar.title()} é de {celsius:.2f}°C ')
        pergunta.pack(padx=10,pady=10)
        print()

    except KeyError:
        problema = tk.Label(janela2, text='Error \nVerifique a conexão ou o texto digitado')
        problema.pack(padx=10, pady=10)

    

#Cria a janela
janela=ctk.CTk()
    
#Deine o tamanho da janela
janela.geometry('250x250')
janela.resizable(False,False)

#Muda o nome da janela
janela.title('XD')

#Texto de boas vindas
texto=ctk.CTkLabel(janela,text='Bem vindo ao Celsius')
#Colocar na janela
texto.grid(padx=10,pady=10)

#Coloca o texto:
pergunta=ctk.CTkLabel(janela,text='Cidade que voce deseja a temperatura:')
pergunta.grid(padx=10,pady=10)
#Pede a digitacao
digite=ctk.CTkEntry(janela,placeholder_text='Digite aqui...')
digite.grid(padx=10,pady=10)
#Botao para consulta
botao=ctk.CTkButton(janela,text='Consultar',command=leituraPrevisao)
botao.grid()
 
#Mantem a janela em looping
janela.mainloop()


