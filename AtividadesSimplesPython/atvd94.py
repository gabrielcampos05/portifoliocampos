#Gabriel Campos Amaral Ribeiro
#04/06/2023

def escreva(frase):
    t=len(frase)
    a=t+2

    print('~'*a)
    print(f' {frase} ')
    print('~'*a)



#Programa Principal7
frase=str(input('Escreva uma frase:')).strip().capitalize()
escreva(frase)
escreva('pessoal')
escreva('Gabriel Campos')
escreva('Olá')