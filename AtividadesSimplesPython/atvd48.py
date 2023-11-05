#Gabriel Campos Amaral Ribeiro
#16/05/2023

ma=0
me=0
for x in range(0,6+1):
    ano=int(input('Digite o ano de nascimento:'))
    if 2023-ano>=21:
        ma=ma+1
    else:
        me=me+1

print(f'{ma} são maiores')
print(f'{me} são menores')

