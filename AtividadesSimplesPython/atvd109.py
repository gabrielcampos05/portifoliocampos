#Gabriel Campos Amaral Ribeiro
#09/06/2023

import moeda2


preco=float(input('Digite o preço: R$'))

print(f'A metade de {moeda2.moeda(preco)} é {moeda2.metade(preco,True)}')
print(f'O dobro de {moeda2.moeda(preco)} é {moeda2.dobro(preco,True)}')
print(f'Aumento de 50% é {moeda2.aumentar(preco,True)}')
print(f'Redução de 50% é {moeda2.diminuir(preco,True)}')

