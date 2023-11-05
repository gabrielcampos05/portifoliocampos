#Gabriel Campos Amaral Ribeiro
#14/05/2023

#Atividade 44

preco=float(input('Digite o\033[1;33m preço do produto: \033[m'))
op=int(input(' \033[1;34m1- À vista (dinheiro ou cheque)\033[m\n'
             ' \033[1;35m2- À vista cartão\033[m\n'
             ' \033[1;31m3- 2x no credito\033[m\n'
             ' \033[1;32m4- 3x ou mais\033[m\n'
             ' Digite:'))

if op==1:
    a=preco*0.90
    print(f'A compra de R${preco}reais vai para R${a}reais')
elif op==2:
    a=preco*0.95
    print(f'A compra de R${preco}reais vai para R${a}reais')
elif op==3:
    print(f'O valor da compra será de R${preco}reais')
    print(f'Parcelamento: 2x de R${preco/2}reais')
else:
    a=preco*1.20
    p=int(input('Quantas vezes vai parcelar? '))
    print(f'A compra de R${preco} reais vai para R${a} reais')
    print(f'Parcelamento: {p}x de R${a/p} reais')
