#Gabriel Campos Amaral Ribeiro
#13/05/2023

d=int(input('Digite a distancia da sua viagem em km:'))

if d<=200:
    print(f'Distancia:{d}km | O preço da passagem é: {(d*0.50)} reais')
else:
    print(f'Distancia:{d}km | O preço da passagem é: {(d*0.45)} reais')