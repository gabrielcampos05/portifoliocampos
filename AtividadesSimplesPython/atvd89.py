#Gabriel Campos Amaral Ribeiro
#03/06/2023

dados={}
totalgols=0

dados['Nome do Jogador']=str(input('Digite o nome do jogador:')).capitalize().strip()
dados['Partidas']=int(input('Digite o número de partidas jogadas:'))

if dados['Partidas']>0:
    for x in range(dados['Partidas']):
        dados[f'Gols jogo {x}'] = int(input(f'Gols feitos partida {x+1}:'))
        totalgols=totalgols+dados[f'Gols jogo {x}']



    dados['Total Gols']=totalgols

print()
for x,y in dados.items():
    print(f'{x}: {y}')









