#Gabriel Campos Amaral Ribeiro
#08/06/2023


def voto(anoNascimento):

    import datetime
    anoAtual=datetime.date.today().year
    idade=anoAtual-ano

    #Opcional
    if idade == 16 or  idade == 17 or idade > 65:
        return f'Você tem {idade} e é OPCIONAL votar !!!'
    #Negado
    elif idade < 16 :
        return f'Você tem {idade} anos e não precisa votar !!!'
    # Obrigatorio
    elif idade >= 18:
        return f'Você tem {idade} anos e já é OBRIGATORIO votar !!!'


ano=int(input('Digite o ano de seu nascimento: '))
print(voto(ano))
