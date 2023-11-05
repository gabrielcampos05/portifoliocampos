#Gabriel Campos Amaral Ribeiro
#14/05/2023

c1=int(input('Digite o comprimento do lado 1 do triângulo:'))
c2=int(input('Digite o comprimento do lado 2 do triângulo:'))
c3=int(input('Dgite o comprimento do lado 3 do triângulo:'))

if (c1<(c2+c3) and (c2<(c1+c3)) and (c3<(c1+c2)) ):
    print(f'O numeros {c1} {c2} {c3} podem formar um triângulo')

    if ((c1==c2) and (c2==c3) and (c3==c1)):
         print('Este é um \033[1;32mtriângulo Equilatero\033[m')
    elif ((c1!=c2) and (c2!=c3) and (c3!=c1)):
         print('Este é um \033[1;32mtriângulo Escaleno\033[m')
    else:
        print('Este é um \033[1;32mtriângulo Isosceles\033[m')

else:
    print(f'O numeros {c1} {c2} {c3}  NÃO podem formar um triângulo')
