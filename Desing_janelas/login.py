#Gabriel Campos Amaral Ribeiro
#01/70/2023

#Construindo janelas bonitinhas em python

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('dark-blue')

# ctrl + / =comenta tudo

# #Cria a janela
janela=ctk.CTk()

def click():
    print('Fazer Login')

# #Define o tamanho da tela
janela.geometry('500x400')

# #Cria o texto
texto=ctk.CTkLabel(janela,text='Fazer Login')

# #Colocar na janela
texto.pack(padx=10,pady=10)

# #Coloca caixas na janela
email=ctk.CTkEntry(janela,placeholder_text='Seu e-mail')
email.pack(padx='10',pady='10')

#show='' permite esconder a senha
senha=ctk.CTkEntry(janela,placeholder_text='Sua senha',show='*')
senha.pack(padx='10',pady='10')

#Cria um botao estilizado
checkbox=ctk.CTkCheckBox(janela,text='Lembrar Login')
checkbox.pack(padx='10',pady='10')


# #Cria um botao
botao=ctk.CTkButton(janela,text="Login",command=click)
botao.pack(padx='10',pady='10')


# #Permite a janela ficar aberta
janela.mainloop()



