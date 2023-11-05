#Gabriel Campos Amaral Ribeiro
#08/05/2023

#Stings
#Fatiamento de uma string

frase='Gabriel campos'

print(frase[3])
print(frase[::4])

##############Analise de uma string#############################
#len(frase)-Comprimento da string
#frase.count('o')-Contagem de letras especificas
#frase.find('deo')-Mostra onde começa na matriz a palavra
#'Curso' in frase- Procura a palavra dentro da frase

x=len(frase)
print(x)

print(frase.count('a'))

w=frase.find('cam')
print(w)

t='campos' in frase
print(t)

##############Transformação#####################################
#frase.replace('Python','Android')-Troca,reposiciona
#frase.upper()-Maiusculo
#farse.lower()-Minusculo
#frase.capitalize()-Transfroma tudo na string para minusculo menos a primeira letra
#frase.title()-Coloca em maiusculo o inicio de toda palavra na string
#frase.strip()-Remove spaces inuteis
#frase.rstrip()-Remove somente os spaces da direita R-Direita
#frase.lstrip()-Remove somente os spaces da direita l-Esquerda

r=frase.replace('campos','ribeiro')
print(r)

u=frase.upper()
print(u)

g=frase.lower()
print(g)

f=frase.capitalize()
print(f)

e=frase.title()
print(e)

r=frase.strip()
print(r)

###############Divisão##########################################
#frase.split()-Divide toda a frase-Cada palavra vira uma string nova
#'-'.join(frase)-Junta palavras com o que foi escolhido em aspas

a=frase.split()
print(a)

c='-'.join(a)
print(c)





