#Gabriel Campos Amaral Ribeiro
#20/05/2023

somaN=0
conta=0
op=''

maior=0
menor=0
media=0

while op!='n':
    n = int(input('Digite um numero:'))
    op = str(input('Deseja continuar [S/N]?')).lower().strip()

    #Pega o maior e o menor
    if n==0:
     maior=n
     menor=n
    else:
        if n>maior:
          maior=n
        else:
          menor=n

    #Faz a media
    somaN=n+somaN
    conta=conta+1
    media=somaN/conta

print(f'O maior numero digitado foi:{maior} e o menor numero digitado foi:{menor}')
print(f'A média dos numeros digitados é:{media}')

