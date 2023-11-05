#Gabriel Campos Amaral Ribeiro
#15/05/2023

s=0
for x in range (1,500+1):
    if(x%2==1):
        if(x%3==0):
          s+=x

print(f'A soma de todos os numeros impares multiplos de três é \033[1;32m{s}\033[m')

