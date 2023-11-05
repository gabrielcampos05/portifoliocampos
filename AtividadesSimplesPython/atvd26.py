#Gabriel Campos Amaral Ribeiro
#13/05/2023

salario=int(input('Digite seu salario:'))

if salario<=1250:
    print(f'Seu salario recebeu um aumento de 15%,Salario Antigo:{salario} | Salario Atual:{salario*1.15} ')
else:
    print(f'Seu salario recebeu um aumenro de 10%,Salario Antigo:{salario} | Salario Atual:{salario*1.10}')