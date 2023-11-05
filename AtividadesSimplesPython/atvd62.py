#Gabriel Campos Amaral Ribeiro
#24/05/2023

total=0
maismil=0
menor=0
cont=0
nomemenor=''
while True:
    print('.' * 30)
    nome=str(input('Nome:')).strip().title()
    preco=float(input('Preço:'))
    cont=cont+1

    #[a]
    total=total+preco

    #[b]
    if preco>1000:
        maismil=maismil+1

    #[c] Mais barato
    #Utiliza-se contador
    if cont==1:
        menor=preco
        nomemenor=nome
    else:
       if preco<menor:
           menor=preco
           nomemenor = nome

    print('.' * 30)
    continuar=str(input('Deseja cadastrar mais produtos?[S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        print('.' * 30)
        continuar = str(input('Deseja cadastrar mais produtos?[S/N]:')).strip().upper()[0]
    if continuar=='N':
        print('.'*30)
        print(f'O total gasto na compra é de R${total:.2f} reais')
        print(f'A quantidade de produtos que custam mais de R$ 1000.00 é: {maismil}')
        print(f'O nome do produto mais barato é {nomemenor}')
        break




