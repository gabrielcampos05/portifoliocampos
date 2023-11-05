#Gabriel Campos Amaral Ribeiro
#09/06/2023

lista=[]
def ficha(nome='',gols=0):
    """

    :param nome: Nome do atleta
    :param gols: Quantidade de gols
    :return: Retorna a ficha
    """

    if nome=='':
        nome='<desconhecido>'
    if gols=='':
        gols=0

    lista.append(nome)
    lista.append(gols)
    print(f'O jogador {lista[0]} fez {lista[1]} gol(s).')

    return ficha




#Programa principal
nome = str(input('Nome: ')).capitalize().strip()
gols = str(input('Gols: '))
ficha()
