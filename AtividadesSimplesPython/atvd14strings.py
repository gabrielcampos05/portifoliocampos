#Gabriel Campos Amaral Ribeiro
#12/05/2023

#Curso Python 09

#Pede o nome completo pra o usuario e tira os espaços inuteis
nome=str(input("Digite seu nome completo:")).strip()

#Transforma o nome para maiusculo
a=nome.upper()

#Transforma o nome para minusculo
b=nome.lower()

#Conta o numero de letras do nome
c=len(nome)
#Conta o numero de espaços
p=nome.count(" ")
#Subtrai o numero de espaços
w=c-p

#Divide o nome,seleciona o primero e faz a contagem
d=nome.split()
e=d[0]
f=len(e)



print(f"O nome com todas as letras maiusculas: {a}")
print(f"O nome com todas as letras minusculas: {b}")
print(f"O nome todo tem {w} letras")
print(f"O primeiro nome tem {f} letras")

print("Outra forma de aprensentação")
#Outra forma de apresentar os dados para o usuario
print(f"O nome maiusculo é: {(nome.upper())}")
print(f"O nome minusculo é: {(nome.lower())}")
print(f"O numero de espaços é: {(len(nome)-nome.count(' '))}")
print(f"O numero de letras do primeiro nnome é:{(nome.find(' '))}")