#Gabriel Campos Amaral Ribeiro
#16/05/2023


for a in range(10):
    frase = str(input('Digite um frase:')).strip()

    #Tira os espaços
    z=frase.replace(" ", "")

    # Inverte a frase
    inverte = z[::-1]

    if (inverte==z):
     print(f'{frase} é um palindromo')
    else:
     print(f'{frase} não é um palindromo')