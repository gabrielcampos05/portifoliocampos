#Gabriel Campos Amaral Ribeiro
#25/05/2023

tabela='Cruzeiro','Grêmio','Athetico','Botafogo','Vitória','Goiás','Santos','Chapecoense','São Paulo','Corinthians','Coritiba','Bahia','Internacional','Criciúma','Fluminense','Flamengo','Portuguesa','Vasco','Náutico','Atlético-MG'

print(f'O top-5 do brasileirão de 2013 foi: {tabela[0]}, {tabela[1]}, {tabela[2]}, {tabela[3]} e {tabela[4]}')
print(f'O Z-4 do brasileirão de 2013 foi:  {tabela[-4]}, {tabela[-3]}, {tabela[-2]} e {tabela[-1]}')

#Sorted=Lista alfabetica
ordemAlfabetica = sorted(tabela)
print(f'Os times em ordem alfabetica é : {ordemAlfabetica}')

#Index busca pela posição
a=tabela.index('Chapecoense')
print(f'A chape esta ficou em: {a}º lugar')