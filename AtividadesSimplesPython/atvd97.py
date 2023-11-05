#Gabriel Campos Amaral Ribeiro
#05/06/2023

numeros=[]

def sorteia():
    import random

    for x in range (5):
        nums=random.randint(1,99)
        numeros.append(nums)
        print(f'{nums}',end=' ')
    print()


def somaPar():

    soma=0
    for nums in numeros:
        if nums%2==0:
            soma=soma+nums
    print(f'A soma de todos os pares é: {soma}')




sorteia()
somaPar()