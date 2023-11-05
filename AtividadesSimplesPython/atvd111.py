#Gabriel Campos Amaral Ribeiro
#10/06/2023

try:
    a=int(input('Numerador:'))
    b=int(input('Denominador:'))
    r=a/b

except (ValueError,TypeError):
    print('Probelmas com o tipo de dado digitado')

except ZeroDivisionError:
    print('Não podemos dividir por zero')

except KeyboardInterrupt:
    print('Preferiu pular')

except Exception as erro:
    print(f'Problema: {erro.__cause__}')

else:
    print(r)

finally:
    print('Volte sempre')
