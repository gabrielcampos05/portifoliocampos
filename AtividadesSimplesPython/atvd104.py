#Gabriel Campos Amaral Ribeiro
#09/06/2023

dicionario={}

def estetica():
    print('='*30)


def notas(*notas,situacao=False):
    """

    :param notas:Recebe as notas do aluno
    :param situacao: Valor opcional para saber os status do aluno
    :return: retorna muitos dados sobre as situações do aluno
    """

    soma=0
    maior=0
    menor=0

    dicionario['Quantidade de notas']=int(input('Quantidade de notas: '))

    #Recebe as notas
    for x in range(dicionario['Quantidade de notas']):
        nota=float(input(f'Nota {x+1}: '))
        dicionario[f'Nota{x}']=nota
        soma=soma+nota

    #Pega o maior e o menor
        if x==0:
            maior=nota
            menor=nota
        else:
            if nota>maior:
                maior=nota
            if nota<menor:
                menor=nota


    # Maior nota
    dicionario['Maior Nota'] = maior

    # Menor nota
    dicionario['Menor Nota'] = menor

    #Calcula a média
    dicionario['Media']=soma/dicionario['Quantidade de notas']


    #Mostra a situação
    consultar = str(input('Deseja ver a situação?[S/N]: ')).upper().strip()[0]

    if consultar == 'S':
    # Define a situação
        if dicionario['Media'] >= 8:
            dicionario['Situação'] = 'BOA'
        if dicionario['Media'] >= 6 and dicionario['Media'] < 8:
            dicionario['Situação'] = 'NA MÉDIA'
        if dicionario['Media'] < 6:
            dicionario['Situação'] = 'RUIM'

        print(dicionario)

    else:
        print(dicionario)


    estetica()
    for x,y in dicionario.items():
        print(f'{x}: {y}')

    return notas




#Programa principal
notas()
#help(notas)




