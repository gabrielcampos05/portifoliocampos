#Gabriel Campos Amaral Ribeiro
#19/07/2023

#Tela de Login com CustomTkinter fazendo a relacao com banco de dados
#Possui alguns erros que nao consegui resolver 


import customtkinter as ctk 
import tkinter as tk
from tkinter import messagebox
import sqlite3

conn=None

# Função para criar a base de dados
def criaDataBase():
    #Cria o Data Base
    conn = sqlite3.connect("LoginCadastroUsers.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Senha TEXT NOT NULL,
        Confirmacao TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Função para desconectar do banco de dados
def desconectaDb():
    conn.close()

# Função para cadastrar o usuário no banco de dados
def cadastrarUsuario():
    lernome = nome.get()
    leremail = email.get()
    lersenha = senha.get()
    lersenha2 = senha2.get()

    if lernome == '' or leremail == '' or lersenha == '' or lersenha2 == '':
        messagebox.showerror(title='ERROR', message='Preencha todos os campos!')
    elif len(lernome) < 4:
        messagebox.showwarning(title='WARNING', message='Nome de usuário deve conter pelo menos 4 caracteres.')
    elif len(lersenha) < 8:
        messagebox.showwarning(title='WARNING', message='Sua senha deve conter pelo menos 8 caracteres.')
    elif lersenha != lersenha2:
        messagebox.showerror(title='WARNING', message='As senhas não correspondem.')
    else:
        conn = sqlite3.connect("LoginCadastroUsers.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Usuarios (Username, Email, Senha, Confirmacao) VALUES (?, ?, ?, ?)
        ''', (lernome, leremail, lersenha, lersenha2))
        conn.commit()
        messagebox.showinfo(title='Register', message=f'{lernome}, seus dados foram criados com sucesso!')
        desconectaDb()
        limpa_dados_cadastro()

# Função para verificar o login do usuário
def verificaLogin():
    leruser = user.get()
    lersenha = ssenha.get()

    conn = sqlite3.connect("LoginCadastroUsers.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Usuarios WHERE (Username=? AND Senha=?)
    ''', (leruser, lersenha))

    verificaDados = cursor.fetchone()  # Percorre o banco de dados

    if lersenha == '' or leruser == '':
        messagebox.showwarning(title='Warning', message='Usuário ou senha vazios')
    elif verificaDados is not None:
        messagebox.showinfo(title='Sucesso', message='Próxima página está em construção, seu login está concluído')
        limpa_entrada_login()
    else:
        messagebox.showerror(title='ERROR', message='Verifique a senha ou o usuário.')
        limpa_entrada_login()

    conn.close()

# Função para limpar os campos de cadastro
def limpa_dados_cadastro():
    nome.delete(0, tk.END)
    email.delete(0, tk.END)
    senha.delete(0, tk.END)
    senha2.delete(0, tk.END)

# Função para limpar os campos de login
def limpa_entrada_login():
    user.delete(0, tk.END)
    ssenha.delete(0, tk.END)

# Função para fechar a janela
def closeJanela(janela):
    janela.destroy()

#------------------------------Cadastro----------------------------------#
def telaCadastroUser():
    global nome, email, senha, senha2

    #Cria a segunda janela
    janela2=ctk.CTk()
    #Define o titlo da segunda janela
    janela2.title('Cadastro')
    #Define o tamanho 
    janela2.geometry('350x400')
    #Impede que o tamanho da janela seja modificado
    janela2.resizable(False,False)
    #Define o icone da pagina
    janela2.iconbitmap('projetosPython\sitemadeLogin\login.ico')

    #Cria os campos para serem cadastrados
    text=ctk.CTkLabel(janela2,text='CADASTRE-SE:',font=('Century Gothic',14,'bold'))
    text.pack(padx=10,pady=10)

    #Nome
    nome=ctk.CTkEntry(janela2,placeholder_text='Your Name',font=('Century Gothic',14,'bold'))
    nome.pack(padx=10,pady=10)

    #Email
    email=ctk.CTkEntry(janela2,placeholder_text='Your Email',font=('Century Gothic',14,'bold'))
    email.pack(padx=10,pady=10)

    #Senha
    senha=ctk.CTkEntry(janela2,placeholder_text='Your password',show='*',font=('Century Gothic',14,'bold'))
    senha.pack(padx=10,pady=10)

    #Confirma Senha
    senha2=ctk.CTkEntry(janela2,placeholder_text='Confirm your password',show='*',font=('Century Gothic',14,'bold'))
    senha2.pack(padx=10,pady=10)

    #CheckBox para ver senha
    versenha=ctk.CTkCheckBox(janela2,text='Vizualizar Senha',font=('Century Gothic',14,'bold'),corner_radius=15)#command=verSenha)
    versenha.pack(padx=10,pady=10)

    #Botao cadastrar
    cadastarTrue=ctk.CTkButton(janela2,text='Cadastrar User',command=cadastrarUsuario,font=('Century Gothic',14,'bold'),corner_radius=15)
    cadastarTrue.pack(padx=10,pady=10)

    #Botao para voltar login
    voltar = ctk.CTkButton(janela2, text='Return Login', command=lambda: closeJanela(janela2),font=('Century Gothic',14,'bold'),fg_color='green',hover_color='#050',corner_radius=15)
    voltar.pack(padx=10, pady=10)

    #Deixa a janela2 aberta 
    janela2.mainloop()

# Criação da janela principal
janela = ctk.CTk()
#Define o tamanho da janela
janela.geometry('350x400')
#Impede a janela de movimentar
janela.resizable(False, False)
#Titulo da janela
janela.title('Login')
#Coloca icone na pagina
janela.iconbitmap('projetosPython\sitemadeLogin\login.ico')

# Cria a base de dados
criaDataBase()

# Espaço para usuário
text = ctk.CTkLabel(janela, text='LOGIN:', font=('Century Gothic', 14, 'bold'))
text.pack(padx=10, pady=10)

# Caixinhas para inserir os dados
user = ctk.CTkEntry(janela, placeholder_text='Your Email ', font=('Century Gothic', 14, 'bold'))
user.pack(padx=10, pady=10)

ssenha = ctk.CTkEntry(janela, placeholder_text='Your Password', show='*', font=('Century Gothic', 14, 'bold'))
ssenha.pack(padx=10, pady=10)

vizusenha = ctk.CTkCheckBox(janela, text='Visualizar Senha', font=('Century Gothic', 14, 'bold'), corner_radius=15)
vizusenha.pack(padx=10, pady=10)

login = ctk.CTkButton(janela, text='Fazer Login', command=verificaLogin, font=('Century Gothic', 14, 'bold'), corner_radius=15)
login.pack(padx=10, pady=10)

cadastro = ctk.CTkButton(janela, text='Realizar Cadastro', fg_color='green', hover_color='#050',font=('Century Gothic', 14, 'bold'), command=telaCadastroUser, corner_radius=15)
cadastro.pack(padx=10, pady=10)

#Deixa a janela aberta 
janela.mainloop()
