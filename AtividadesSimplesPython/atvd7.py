largura=int(input('Digite a largura da parede:'))
altura=int(input('Digite a altura da parede:'))

area=largura*altura

tinta=area/2

print(f'É necessario {tinta} litros para pintar {area} m2')

########################################################

preco=float(input('Digite um preço:'))

desconto=1.00-0.05

final=preco*desconto

print(f'O valor final apos o desconto de 5% foi:{final}')

##########################################################

salario=float(input('Digite seu salario:'))

aumento=1.00+0.15

sfinal=salario*aumento

print(f'O salario apos o aumento foi de {sfinal}')

