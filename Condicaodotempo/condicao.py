#Gabriel Campos Amaral Ribeiro
#03/07/2023

#Previsao do tempo com API
import requests as rq

def conversao(kelvin):
    celsius = kelvin - 273.15
    return celsius

key='88f9ee706197160c65aff2e93f7c0e19'

print('\033[1;33mBem vindo ao programa de consulta do tempo\033[m')
city=str(input('Digite o nome da cidade: '))

link=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=pt_br'

requisicao=rq.get(link)

dados=requisicao.json()
descricao=dados['weather'][0]['description']
temperatura=dados['main']['temp']

celsius=conversao(temperatura)


print(f'Condição:{descricao} e a temperatura em {city.title()} é de {celsius:.2f}°C')
print()

