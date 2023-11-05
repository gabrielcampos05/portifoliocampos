#Gabriel Campos Amaral Ribeiro
#03/06/2023

def mostraLinha():
    print('='*30)

def mensagem(msg):
    print('/' * 30)
    print(msg)
    print('/' * 30)
mensagem('Sistema')
mensagem('OI')


mostraLinha()
print('OI')
mostraLinha()


def soma(a,b):
    s=a+b
    print(s)

#a=int(input('Digite um numero:'))
#b=int(input('Digite outro numero:'))
#soma(a,b)


#Transforma o contador em uma tupla
def contador(*num):
    tamanho=len(num)
    #print(tamanho)
    #print(f'Recebi {num} e possuem {tamanho}')


contador(1,2,3,4,5,6)
contador(7,8,9,10,11,12)


def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
    print(val)


val=[1,2,3,4,5]
print(val)
dobra(val)






