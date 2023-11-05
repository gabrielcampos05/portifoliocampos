#Relacionado a atividade 107


#Aumento de 50%
def aumentar(preco):
    return preco*1.50


#Redução de 50%
def diminuir(preco):
    return preco*0.50


def dobro(preco):
    return preco*2


def metade(preco):
    return preco/2

#Faz parte da atividade 108
def moeda(preco,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

#Faz parte da atividade 110
def resumo(preco):
    print(f'{metade(preco)}')
    print(f'{dobro(preco)}')
    print(f'{diminuir(preco)}')
    print(f'{aumentar(preco)}')


