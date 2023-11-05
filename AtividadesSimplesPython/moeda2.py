#Relacionado a atividade 107 e 109


#Aumento de 50%
def aumentar(preco,formatacao=False):
    return preco*1.50 if formatacao==False else moeda(preco)


#Redução de 50%
def diminuir(preco,formatacao=False):
    return preco*0.50 if formatacao is False else moeda(preco)


def dobro(preco,formatacao=False):
    return preco*2 if formatacao is False else moeda(preco)


def metade(preco,formatacao=False):
    return preco/2 if formatacao is False else moeda(preco)

#Faz parte da atividade 108
def moeda(preco,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
