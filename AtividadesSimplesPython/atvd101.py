#Gabriel Campos Amaral Ribeiro
#08/06/2023


def fatorial(num,show=False):
    """

    :param num: Número que se deseja o fatorial
    :param show: Ver ou não a sequência fatorial
    :return: Retorna o fatorial

    """
    f=1
    for x in range(num,0,-1):

        if show==True:
            print(f'{x}',end='')
            if x>1:
                print(f'*',end='')
            if x==1:
                print(f'=',end='')

        f=f*x
    return f



n=int(input('Digite um num: '))
a=str(input('Deseja ver a saida da sequencia do fatorial?[S/N]: ')).strip().upper()[0]

if a=='S':
    print(fatorial(n, show=True))
else:
    print(fatorial(n, show=False))

#help(fatorial)



