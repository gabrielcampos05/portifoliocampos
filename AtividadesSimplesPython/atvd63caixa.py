#Gabriel Campos Amaral Ribeiro
#24/05/2023

print('====Bem vindo(a)====')
valor=int(input('Digite o valor que deseja sacar R$'))

#Primeiro tira o valor da divisão inteira
#1234//50=24
d1=valor//50
#Subtrai o inteiro da divisão pelo valor total
#50*24=1200-1234=34
a=valor-(d1*50)

d2=a//20
b=valor-(d1*50)-(d2*20)

d3=b//10
c=valor-(d1*50)-(d2*20)-(d3*10)

d4=c//1
d=valor-(d1*50)-(d2*20)-(d3*10)-(d4*1)

print('.'*30)
print('\033[1;32mRESULTADO DO SAQUE:\033[m')
print('.'*30)
if d1>0:
    print(f'[{d1}] notas de R$50.00')
if d2>0:
    print(f'[{d2}] notas de R$20.00')
if d3>0:
    print(f'[{d3}] notas de R$10.00')
if d4>0:
    print(f'[{d4}] notas de R$1.00')
print('.'*30)
