#Gabriel Campos Amaral Ribeiro
#14/05/2023

#Condições Aninhadas

valor=float(input('Digite o \33[1;31m valor da casa \033[m:'))
salario=float(input('Digite o \33[1;31m seu salario \033[m:'))
ano=int(input('Digite em \33[1;31m quantos anos \033[m voce pagará?'))

conversao=ano*12
parcelas=valor/conversao
condicao=salario*(30/100)


if parcelas>=condicao:
    print(f'\033[1;31m Emprestimo negado \033[m')
else:
    print(f'\033[1;32m Emprestimo aprovado \033[m !!! Valor da casa:{valor} | Salario:{salario} | Anos de pagamento:{ano} | \033[1;32m Valor das parcelas:{parcelas} \033[m')