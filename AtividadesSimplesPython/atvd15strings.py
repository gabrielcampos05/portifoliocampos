#Gabriel Campos Amaral Ribeiro
#12/05/2023


nome=str(input('Digite o nome de uma cidade:')).strip()

#Passa para maiusculo
x=nome.upper()

#Separa a palavra
xx=x.split()

#Pega a primeira
xxx=xx[0]

#Verifica se tem a palavra
txt='SANTO' in xxx

print(f'A cidade começa com Santo? {(txt)}')



