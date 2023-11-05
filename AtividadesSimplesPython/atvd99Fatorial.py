#Gabriel Campos Amaral Ribeiro
#08/06/2023

def fatorial(num=1):
    f=1
    for x in range(num,0,-1):
        f=f*x
    return f

n=int(input('Digite um num:'))
print(fatorial(n))
