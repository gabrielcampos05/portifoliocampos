#Gabriel Campos Amaral Ribeiro
#14/05/2023

idade=int(input('Digite a idade:'))

if idade<=9:
    print('\033[1;33m MIRIM \033[m')
elif idade>9 and idade<=14:
    print('\033[1;33m INFANTIL \033[m')
elif idade>14 and idade<=19:
    print('\033[1;33m JUNIOR \033[m')
elif idade==20:
    print('\033[1;33m SÊNIOR \033[m')
else:
    print('\033[1;33m MASTER \033[m')

