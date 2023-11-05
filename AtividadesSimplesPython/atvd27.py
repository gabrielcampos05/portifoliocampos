#Gabriel Campos Amaral Ribeiro
#13/05/2023

c1=int(input('Digite o comprimento do lado 1 do triangulo:'))
c2=int(input('Digite o comprimento do lado 2 do triangulo:'))
c3=int(input('Dgite o comprimento do lado 3 do triangulo:'))

if (c1<(c2+c3) and (c2<(c1+c3)) and (c3<(c1+c2)) ):
    print(f'O numeros {c1} {c2} {c3}  podem formar um triangulo')
else:
    print(f'O numeros {c1} {c2} {c3}  NÃO podem formar um triangulo')

