#Gabriel Campos Amaral Ribeiro
#16/05/2023

media=0
y=0
s=0
velho=0
nomevelho=''

for x in range(1,5):
    nome=str(input(f'Digite nome do {x}º:'))
    idade=int(input(f'Digite a idade do {x}º:'))
    sexo=str(input(f'Digite o sexo do {x}º:'))

    #Calcula a media
    y+=idade
    media=y/x

    #Pega a idade só de homem
    #Comparação USAR COMO PADRAO
    if sexo=='masculino':
        if x==1:
            velho=idade
            nomevelho=nome
        elif idade>velho:
             velho=idade
             nomevelho=nome
    #Conta a quantidade mulher com menos de 20anos
    elif sexo=='feminino':
      if idade<20:
         s=s+1

print(f'\033[1;33mA media das idades é: {media} anos\033[m')
print(f'\033[1;33mA quantidade de mulheres que tem menos de 20 anos é {s}\033[m')
print(f'\033[1;33mO nome do homem mais velho é:{nomevelho}\033[m')