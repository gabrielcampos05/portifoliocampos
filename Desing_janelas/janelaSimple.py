#Gabriel CAmpos Amaral Ribeiro
#07/07/2023

#Janelas com PySimpleGUI
#Consulta sobre a cotacao de moedas

import PySimpleGUI as sg 
import requests

def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None

import PySimpleGUI as sg

layout = [
    [sg.Text('Pegar cotação da moeda')],
    [sg.InputText(key='moeda')],
    [sg.Button('Pegar cotação'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
]

janela = sg.Window('Sistema de cotações', layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break

    if evento == "Pegar cotação":
        codigo= valores['moeda']
        cotacao=pegar_cotacoes(codigo)
        janela['texto_cotacao'].update(f'A cotacao do {codigo} é de R${cotacao}')

janela.close()
