#Gabriel Campos Amaral Ribeiro
#21/05/2023

while True:
    n=int(input('Digite o numero que você deseja a tabuada:'))
    #Condição parada
    if n<0:
        break

    for x in range (1,10):
        tabuada=x*n
        print(f'{n} x {x} = {tabuada}')
    print('='*20)


print('\033[1;31mEncerrado \033[m')
