#Gabriel Campos Amaral Ribeiro
#13/05/2023

nome=str(input('Digite seu nome nome completo:')).strip()

#Separa o nome
x=nome.split()
#Pega o primeiro nome
y=x[0]
print(nome.title())
print(f'Primeiro nome:{y.title()}')

#Pega o ultimo nome
z=x[-1]
print(f'Ultimo nome:{z.title()}')

