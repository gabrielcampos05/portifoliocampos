#Gabriel Campos Amaral Ribeiro
#13/05/2023

velocidade=int(input('Digite a velocidade do carro:'))

if velocidade>80:
    print('Você ultrapasssou o limite de velocidade!')
    print(f'Foi multado em {((velocidade-80.00)*7.00)} reais')
else:
    print('Você não foi multado!')