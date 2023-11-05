#Gabriel Campos Amaral Ribeiro
#09/07/2023

#Projeto 1 
#Calculadora com TkCustom


import customtkinter as ctk 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()


        #Visor superior da calculadora 
        self.frame=ctk.CTkFrame(self,width=300, height=50,fg_color='#116',corner_radius=0)
        self.frame.pack()
        self.lb_title=ctk.CTkLabel(self.frame,text='Simple Calculator',font=('Roboto bold',20))
        self.lb_title.place(x=70,y=10)

        self.span=ctk.CTkLabel(self,text='Esta é uma simples calculadora,nao exija muito dela!')
        self.span.pack()

        #Entrada de dados
        self.entry=ctk.CTkEntry(self,width=250,font=('Roboto bold',18))
        self.entry.pack(pady=20)

        self.result=ctk.CTkLabel(self,text='',text_color='teal',font=('Roboto bold',20))
        self.result.pack()

        self.btn=ctk.CTkButton(self,width=250,text='Calcular'.upper(),command=self.calcular)
        self.btn.pack(pady=20)

    def calcular(self):
        self.result.configure(text=str(eval(self.entry.get())))


app=App()
#Define o tamnho da janela
app.geometry('300x300')
#Da o titulo para janela
app.title('Simple Calculator')
#Limita o tamnho da janela
app.resizable(False,False)
#Deixa a janela aberta
app.mainloop()





# print('Calculadora basica')

# num=float(input('Digite um num:'))

# print()
# print('[1] - Soma;')
# print('[2] - Subtracao;')
# print('[3] - Divisao;')
# print('[4] - Multiplicacao;')
# print()

# op=int(input('Escolha a operacao:'))

# while op<0 or op>4:
#     op=int(input('Escolha a operacao:'))



# num2=float(input('Digite um num:'))


# if op==1:
#     print(f'{num}+{num2}={num+num2}')
#     print()

# if op==2:
#     print(f'{num}-{num2}={num-num2}')
#     print()

# if op==3:
#         try:
#              print(f'{num}/{num2}={num/num2}')
#              print()

#         except ZeroDivisionError:
#             print('ERROR')
#             print('Divisao por zero paizao??? pqp')


# if op==4:
#     print(f'{num}x{num2}={num*num2}')
#     print()

