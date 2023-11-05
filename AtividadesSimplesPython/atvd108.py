#Gabriel Campos Amaral Ribeiro
#09/06/2023

import moeda


preco=float(input('Digite o preço: R$'))


print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumento de 50% é {moeda.moeda(moeda.aumentar(preco))}')
print(f'Redução de 50% é {moeda.moeda(moeda.diminuir(preco))}')