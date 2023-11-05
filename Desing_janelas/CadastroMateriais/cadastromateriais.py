#Gabriel Campos Amaral Ribeiro
#03/07/2023

import customtkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt 

import dataBaser

def click():

    print('Objeto catalogado')



def RegistroDataBase():

    Descricao=digitar.get()
    Tipo=combobox.get()
    Quantidade=digite.get()

    
    
    dataBaser.cursor.execute('''
    INSERT INTO Users(Descricao,Tipo,Quantidade) VALUES(?,?,?)
    ''',(Descricao,Tipo,Quantidade))
    dataBaser.conn.commit()

    messagebox.showinfo(title='Register',message='Produtos registrados') 



#Define cor
tk.set_appearance_mode("dark")
tk.set_default_color_theme('dark-blue')

#Define a lista de materiais do cadastro
lista_tipos=['Galão','Caixa','Unidade','Saco','Garrafa']
lista_codigos=[]


#Cria a janela
janela=tk.CTk()

# #Define o tamanho da tela
janela.resizable(width=False, height=False)  #Impede a redimensionamento da janela
janela.geometry("350x300")  # Define o tamanho da janela


#Titulo da janela 
janela.title('Cadastro')

###################################################################################

#Cria a parte de descricao dos materiais
descricao=tk.CTkLabel(janela,text='Descrição do material:')
descricao.grid(row=1,column=0,padx=10,pady=10,sticky='nswe',columnspan=4)
#Espaco para o usuario digitar a descricao do produto
digitar=tk.CTkEntry(janela)
digitar.grid(row=2,column=0,padx=10,pady=10,sticky='nswe',columnspan=4)


#####################################################################################

#Espaco para o usuario digitar o tipo da unidade do produto
unidade=tk.CTkLabel(janela,text='Tipo da unidade do material:')
unidade.grid(row=3,column=0,padx=10,pady=10,sticky='nswe',columnspan=2)
#Espaco para o usuario digitar o tipo da unidade do produto dentro de uma caixa  # TTK ajuda na estilizacao
combobox=ttk.Combobox(janela,values=lista_tipos)
combobox.grid(row=3,column=2,padx=10,pady=10,sticky='nswe',columnspan=2)

#######################################################################################

#Espaco para o usuario digitar a quantidade dpo tipo de unidades
quantidade=tk.CTkLabel(janela,text='Quantidade:')
quantidade.grid(row=4,column=0,padx=10,pady=10,sticky='nswe',columnspan=2)
#Espaco para o usuario digitar a descricao do produto
digite=tk.CTkEntry(janela)
digite.grid(row=4,column=2,padx=10,pady=10,sticky='nswe',columnspan=2)

#########################################################################################
#Botao cadastro
botao=tk.CTkButton(janela,text="Catalogar",command=RegistroDataBase)
botao.grid(row=5,column=0,padx=10,pady=10,sticky='nswe',columnspan=4)

#Mudar icone da pagina 
janela.iconbitmap('projetosPython\desing_janelas\midia\estoque2.ico')

#Deixa a janela aberta
janela.mainloop()