#Gabriel Campos Amaral Ribeiro
#03/06/2023


dados={}
lista=[]
totalgols=0

while True:

    dados['Nome do Jogador']=str(input('Digite o nome do jogador:')).capitalize().strip()
    dados['Jogos']=int(input('Digite o número de partidas jogadas:'))

    if dados['Jogos']>0:
        for x in range(dados['Jogos']):
            dados[f'Gols jogo {x}'] = int(input(f'Gols feitos partida {x+1}: '))
            totalgols=totalgols+dados[f'Gols jogo {x}']
        dados['Total Gols']=totalgols

    lista.append(dados.copy())

    continuar = str(input('Deseja cadastrar outro jogador?[S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar outro jogador?[S/N]: ')).strip().upper()[0]

    if continuar == 'N':

        tot = len(lista)
        print('*'*30)
        for a,dados in enumerate(lista,1):
            print(f'ID:{a} -- Atleta: {dados["Nome do Jogador"]}')
        print('*' * 30)
        escolha=int(input('Deseja ver as estatisticas de qual jogador?: '))
        print('*' * 30)

        while escolha > tot:
            escolha = int(input('Deseja ver as estatisticas de qual jogador?: '))

        escolha=escolha-1
        jogador=lista[escolha]
        print(f'Analise do atleta: {dados["Nome do Jogador"]}')
        for x in range(jogador['Jogos']):
           print(f'Partida {x+1}: {jogador[f"Gols jogo {x}"]} gols')
        print(f'O total de gols é:{totalgols}')








        break











