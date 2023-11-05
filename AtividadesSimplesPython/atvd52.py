#Gabriel Campos Amaral Ribeiro
#20/05/2023

sexo=str(input('Digite seu sexo [M/F]:')).lower().strip()

#Estrura While para not
while sexo not in 'f' 'm':
    sexo = str(input('Opção invalida.Digite [M/F]:')).lower().strip()

print('Dados registrados!')
