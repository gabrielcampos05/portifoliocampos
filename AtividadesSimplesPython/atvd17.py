#Gabriel Campos Amaral Ribeiro
#13/05/2023

x=str(input('Digite uma frase:')).strip()

#Passa a frase para minuscula
frase=x.lower()
#Conta o numero de A's
y=frase.count('a')
print(f'A letra [A] aparece {y} veze(s)')

#Pega onde começa com A
z=frase.find('a')
print(f'A primeira letra [a] se encontra na posição:{z}')

#Pega a ultima letra A
w=frase.rfind('a')
print(f'A ultima letra [a] se encontra na posição:{w}')



