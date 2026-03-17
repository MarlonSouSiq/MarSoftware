import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    #print(texto)
    texto_cotacoes["text"]=texto

    

janela=Tk()
janela.title("Cotação Atual das moedas")
janela.geometry("400x400")
janela.configure(bg='blue')

texto_orientacao=Label(janela,text="Clique no botão para ver a cotação",font="arial")
#texto_orientacao.grid(column=0, row=0)
texto_orientacao.pack(pady=20)


botao= Button(janela, text="Buscar Cotações Dolar, Euro, Bitcoin", command=pegar_cotacoes) # pegar_cotação sem parentes, pois se colocar executa na hora
#botao.grid(column=0,row=1)
botao.pack(pady=20)

texto_cotacoes=Label(janela,text="")
texto_cotacoes.pack(pady=20)

janela.mainloop()

