#Gabriel Campos Amaral Ribeiro
#14/05/2023

peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura:'))

imc=(peso/(altura*altura))

if imc<18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso ideal')
elif imc>=25 and imc<30:
    print('Sobrepeso')
elif imc>=30 and imc<40:
    print('Obesidade')
else:
    print('Obesidade morbida')

print(f'IMC:{imc}')