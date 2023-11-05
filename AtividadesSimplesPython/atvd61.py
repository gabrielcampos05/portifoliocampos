#Gabriel Campos Amaral Ribeiro
#24/05/2023

#ATIVIDADE 69
mais18=0
homem=0
mulher=0
while True:


    idade=int(input('Idade:'))

    sexo=str(input('Sexo[M/F]:')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]:')).strip().upper()[0]

    if idade>=18:
        mais18=mais18+1
    if sexo=='M':
        homem=homem+1
    elif sexo=='F':
        if idade<=20:
            mulher=mulher+1


    continuar=str(input('Quer cadastratar mais pessoass?[S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer cadastratar mais pessoass?[S/N]:')).strip().upper()[0]
    if continuar=='N':
        print('~~' * 30)
        print(f'Pessoas com mais de 18 anos: {mais18}')
        print(f'Quantidade de homens: {homem}')
        print(f'Quantidade de mulheres com menos de 20 anos: {mulher}')
        break








