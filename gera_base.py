# codigo para gerar uma base, no final abre em uma janela.


import random
from datetime import datetime,timedelta
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def gerabase(quantidade=100):
    bairro=['Andarai','Meier','Barra da Tijuca','Copacabana','Irajá','Penha','Ramos','Ipanema','Centro','Olaria']
    rua=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
    tecnico=['Marcus Vinicius','Matheus','Vinicius','Antonio','Maria','Cristina','Jose','Walter']
    causa_defeito=['Fibra partida','ONT com defeito','OLT com defeito','Causa cliente','Reconfiguração','Falta de Energia','Serviço Funcionando']

    inicio=datetime(2026,1,1)
    hoje=datetime.now()
    dias_passados=(hoje-inicio).days
    print(dias_passados)

    dados_gerados = []

    for i in range(quantidade):
        end_rua= random.choice(rua)
        end_bairro= random.choice(bairro)
        end_num= random.randint(1,1000)
        tecnico_ins= random.choice(tecnico)
        dias_aleatorios=random.randint(0,dias_passados)  # Determina um valor numerico entre hoje e a data de instalação
        data_ins=inicio +timedelta(days=dias_aleatorios)  # Determina a data depois de inicio + dias aleatorios

        dias_passados_posinst=(hoje-data_ins).days  #Determina os dias entre a data de instalação e hoje
        dias_aleatorios_pos_inst=random.randint(0,dias_passados_posinst) # Determina um valor numerico a data de instalação e hoje
        data_reparo=data_ins +timedelta(days=dias_aleatorios_pos_inst) #Data do reparo é data de ins + número aleatorio
        #print(f'Data de Instalação: {data_ins.date()} e do reparo {data_reparo.date()}')
        tecnico_reparo=random.choice(tecnico)
        tempo_de_reparo=random.randint(1,5)
        reparo= random.choice(causa_defeito)


        dados_gerados.append({
            'ID': i,
            'Rua': end_rua,
            'Numero': end_num,
            'Bairro': end_bairro,
            'Tecnico Ins': tecnico_ins,
            'Data Ins':data_ins.date(),
            'Data Rep': data_reparo.date(),
            'Tecnico Reparo': tecnico_reparo,
            'Tempo Reparo': tempo_de_reparo,
            'Causa Reparo': reparo
            })
    
    return pd.DataFrame(dados_gerados)

#print(gerabase(10))

# mostra resultado em uma janela
janela = tk.Tk()
janela.title("Resultado")
resultado=gerabase(10)
label = tk.Label(janela, text=str(resultado), justify="left")
label.pack(padx=20, pady=20)
janela.mainloop()  