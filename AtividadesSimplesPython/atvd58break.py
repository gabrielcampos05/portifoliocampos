#Gabriel Campos Amaral Ribeiro
#21/05/2023

#while true -> loop infinito
#break interrompe o loop while



s=0
cont=0

#loop infinito com break
while True :
    n=int(input('Digite um numero:'))
    if n==999:
        break

    cont+=1
    s=n+s


print(f'A soma dos {cont} valores deu {s}')




