import requests
from openpyxl import Workbook

lista_moedas = ['USD-BRL','EUR-BRL','BTC-BRL']

moedas = ','.join(lista_moedas)

# Consumir API de cotações.
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/'+moedas)
cotacoes = cotacoes.json()

# Criar planilha excel.
wb = Workbook()
wb.create_sheet('Cotacoes Moedas')
ws = wb['Sheet']

# Linha de título da tabela.
ws.append(['Moeda','Cotação'])

for m in lista_moedas:
    # Preencher linhas de cotações.
    moeda = m.replace('-','')
    ws.append([cotacoes[moeda]['name'], cotacoes[moeda]['bid']])

wb.save("cotacoes.xlsx")
