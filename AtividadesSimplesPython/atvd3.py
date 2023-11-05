a =int(input('Digite um numero:'))
b =int(input('Digite outro numero:'))

soma= int(a) + int(b)

print(f'A soma deu:{soma}')
print('A soma vale:',soma)

print('A soma {}:'.format(soma))

print(f'A soma entre {a} e {b} vale {soma}')
print('A soma entre',a,'e',b,'vale',soma)
print("A soma entre {} e {} vale {}".format(a,b,soma))

#Para obter a classe do numero
print(type(soma))