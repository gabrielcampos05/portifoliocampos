#Gabriel Campos Amaral Ribeiro
#09/06/2023
import moeda


preco=float(input('Digite o preço: R$'))

print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumento de 50% é {moeda.aumentar(preco)}')
print(f'Redução de 50% é {moeda.diminuir(preco)}')

moeda.resumo(preco)



