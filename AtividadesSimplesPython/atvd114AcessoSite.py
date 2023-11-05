#Gabriel Campos Amaral Ribeiro
#10/06/2023

#Biblioteca que permite acessar sites
import requests


# Faz a solicitação para um site
site='http://www.pudim.com.br/'

# Acessa o site
#requests.get()
acesso=requests.get(site)

#Verifica
#status.code
if acesso.status_code==200:
    print('Foi possivel acessar o site')
else:
    print('Erro ao acessar o site')

#site.read()-Lê o site

#######################################
#Outra forma de acessar

#import urllib
#import urllib.request

#try:
#    site=urllib.request.urlopen('http://www.pudim.com.br/')
#except :
#    print('O site não está acessivel no momento')
#else:
#    print('Site acessivel')
#    print(site.read())