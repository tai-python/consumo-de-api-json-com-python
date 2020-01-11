import requests
import json
import pandas
import decimal

url = 'http://data.fixer.io/api/latest?access_key=d08ba93fa0c198100223c4dd8193753b'
print('Acessando base de dados da Fixer.io...')
print('Buscando informações...')
resposta = requests.get(url)
print(resposta)
if resposta.status_code == 200:
    print('Acesso realizado com sucesso!')
    print('Buscando infoormações...')
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'],2)
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'],2)
    btc_real = round(dados['rates']['BRL']/dados['rates']['BTC'],2)
    print('1 dollar vale ',dolar_real, 'reais')
    print('1 euro vale ',euro_real, 'reais')
    print('1 Bitcoin vale ',btc_real, 'reas')
    print('Importando resultado em tabela Excel...')
    tela = pandas.DataFrame({'moedas':['Dolar', 'Euro', 'Bitcoin'], 'vaalores':[dolar_real, euro_real, btc_real]})
    tela.to_csv('valores.csv', index=False, sep=";", decimal=",")
    print('Arquivo exportado com sucesso')
else:
    print('Erro na base de dados')
