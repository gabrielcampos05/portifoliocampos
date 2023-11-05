#Gabriel Campos Amaral Ribeiro
#04/11/2023

#Calculadora de IMC com tkinter
#peso/altura^2

import customtkinter as ctk
import tkinter as tk

#Fechar janela
def close(app2):
    app2.destroy()

def calculoIMC():

    #Pega o que foi digitado nos blocos
    digitePeso=float(peso.get())
    digiteAltura=float(altura.get())
    #Deixa em metros
    AlturaM=digiteAltura/100
    #Calcula IMC
    imc=(digitePeso/(AlturaM**2))
    #Restringe as casas decimais
    imcFinal=f'{imc:.2f}'
    imcFinal = float(imcFinal)



    #Cria a janela
    app2=tk.Tk()
    #Define o tamnho da janela
    app2.geometry('295x230')
    #Da o titulo para janela
    app2.title('IMC')
    #Limita o tamnho da janela
    app2.resizable(False,False)
    #Define cor de fundo
    app2.configure(bg='#313131')

    #Titulo do aplicativo
    top=tk.Label(app2,text=' Resultado do Calculo:')
    top.grid(padx=75,pady=10)
    #Resultado
    resul=tk.Label(app2,text=f'IMC={imcFinal}')
    resul.grid(padx=75,pady=10)

    #Condições de resultado
    if imcFinal<=18.5:
        resul=tk.Label(app2,text='ABAIXO DO PESO')
        resul.grid(padx=75,pady=10)
    elif imcFinal>18.5 and imcFinal<24.9:
        resul=tk.Label(app2,text='NORMAL')
        resul.grid(padx=75,pady=10)
    elif imcFinal>=25 and imcFinal<=29.9:
        resul=tk.Label(app2,text='SOBREPESO')
        resul.grid(padx=75,pady=10)
    elif imcFinal>=30 and imcFinal<=34.9:
        resul=tk.Label(app2,text=' GRAU 1')
        resul.grid(padx=75,pady=10)
    elif imcFinal>=35 and imcFinal<=39.9:
        resul=tk.Label(app2,text='OBESIDADE GRAU 2')
        resul.grid(padx=75,pady=10)
    else:
        resul=tk.Label(app2,text='OBESIDADE MORBIDA')
        resul.grid(padx=75,pady=10)

    #Botao fecha janela
    button2=ctk.CTkButton(app2,text='Fechar janela',command=lambda: close(app2))
    button2.grid()

    #Deixa a janela aberta
    app2.mainloop()

#Definir icons para as janelas e posicionar melhor as caixas e botoes 
############################################################################################  
  

#Cria a janela principal
app=ctk.CTk()
#Define o tamanho da janela
app.geometry('295x230')
#Da o titulo para janela
app.title('Calculator IMC')
#Limita o tamnho da janela
app.resizable(False,False)

#Titulo do aplicativo
top=ctk.CTkLabel(app,text=' Calculadora de IMC')
top.grid(padx=85,pady=10)

#Recepção dos dados do peso
peso=ctk.CTkEntry(app,placeholder_text='Seu peso em kg ...')
peso.grid(padx=40,pady=10)

#Recepção dos dados da altura
altura=ctk.CTkEntry(app,placeholder_text='Sua altura em cm ...')
altura.grid(padx=40,pady=10)

#Botao consulta
button=ctk.CTkButton(app,text='Consultar',command=calculoIMC)
button.grid()

#Deixa a janela aberta
app.mainloop()



