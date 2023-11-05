#Gabriel Campos Amaral Ribeiro
#01/06/2023

lista=[]
a=0
while True:
    nome=str(input('Digite o nome:')).strip().capitalize()
    nota1=float(input('Nota 01:'))
    nota2=float(input('Nota 02:'))
    media=(nota1+nota2)/2

    lista.append([[nome,[nota1,nota2],media]])


    continuar=str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]



    if continuar=='N':
        print('=' * 30)
        for y, nome in enumerate(lista):
            a = lista[y][0][0]
            print(f'{y} ----- {a}')

        print('=' * 30)

        consulta=int(input('Digite o ID para consultar a media:'))
        print('=' * 30)
        print(f'ALUNO: {lista[consulta][0][0]} | NOTAS: {lista[consulta][0][1][0]} e {lista[consulta][0][1][1]} | MÉDIA: {lista[consulta][0][2]}')
        print('='*30)


        break


