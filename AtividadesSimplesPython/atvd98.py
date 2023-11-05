#Gabriel Campos Amaral Ribeiro
#08/06/2023

#Interactive Help

#Pegar a documentação,tirar dúvida sobre
help(print)
print(input.__doc__)

#Docstring

def contador(i,f,p):
#Coloca a documentação na função:["""]
    """
    ->Faz uma contagem e mostra na tela;
    :param i:inico da contagem
    :param f:fim da contagem
    :param p:passoa da contagem
    :return:sem retorno

    """

    c=i
    while f>=c:
        print(f'{c}',end=' ')
        c=c+p
    print('Fim')

print()
contador(0,10,1)

help(contador)

#Parâmetros opcionais
#Iguala a zero para caso não tenha tds os parametros
def somar(a=0,b=0,c=0):
    s=a+b+c
    print(f'{s}')

somar(1,5,6)
somar(1,2)
somar(8)
somar()

#Escopo de variáveis

def teste(b):
    #Global segura a viravel dentro e fora
    global a
    a=8
    b+=4
    c=2
    print()
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a=5
teste(a)
print(f'A fora vale {a}')

#Return
def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

r1=somar(1,5,6)
r2=somar(1,9,7)
r3=somar(9,8,6)
print(f'As somas deram {r1} {r2} e {r3}')

