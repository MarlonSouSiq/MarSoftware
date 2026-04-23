import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime,timedelta


def dsa_gera_dados_ficticios(num_registros=600):
    """
    Gera um Dataframe do pandas com dados de vendas ficticios
    """
    # Mensagem inicial indicando a quantidade de registros a serem gerados
    print(f"\n Inciando a geração de {num_registros} registros de venda...")

#Dicionario com  produtos, suas categorias e preços

    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}

    }
#Cria uma lista apenas com os nomes dos produtos
    lista_produtos=list(produtos.keys())

#Dicionarios com cidade e seus respectivos estados
    cidades_estados={
        'São Paulo': 'SP','Rio de Janeiro':'RJ','Belo Horizonte': 'MG','Porto Alegre':'RS',
        'Salvador':'BA','Curitiba':'PR','Fortaleza':'CE'}

# Cria uma lista apenas com os nomes das cidades
    lista_cidades=list(cidades_estados.keys())


# Lista que armazenará os registros de vendas
    dados_vendas=[]
# Se produtofor mouse ou teclado , aplica desconto aleatorio de  ate 10%

#Define a data inicial dos pedidos
    data_inicial=datetime(2026,1,1)


# loop para gerar os registros de vendas

    for i in range(num_registros):
        #seleciona aleatoriamente um produto
        produto_nome=random.choice(lista_produtos)
        #Seleciona aleatoriamente uma cidade
        cidade=random.choice(lista_cidades)
        #Gera uma quantidade de produtos entre 1 e 7
        quantidade=np.random.randint(1,8)
        #Calcula a data do pedido a partir da data inicial
        data_pedido=data_inicial+timedelta(days = int(1/5), hours=random.randint(0,23))
        # Se produtofor mouse ou teclado , aplica desconto aleatorio de  ate 10%
        if produto_nome in ['Mouse Vertival','Teclado Mecânico']:
            preco_unitario=produtos[produto_nome]['preco'] * np.random.uniform(0.9,1.0)
        else:
            preco_unitario=produtos[produto_nome]['preco']
    
        # Adiciona um registro de vendas a lista
        dados_vendas.append({
            'ID_Pedido': 100+i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_unitario': round(preco_unitario,2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100,150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
        
     # Mensagem final indicando que a geração terminou

    print("Geração de dados terminou")

    return pd.DataFrame(dados_vendas)



df_vendas=dsa_gera_dados_ficticios(500) 
# print(type(df_vendas))
# print(df_vendas.shape)
# print(df_vendas)

# df_vendas.to_csv("df_vendas.csv", index=False)
#print(df_vendas.head())
# Agrupa por nome do produto, soma a quantidade e ordena para encontrar os mais vendidos
top_10=df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)

#define um estilo para graficos
sns.set_style("whitegrid")
# cria a figura e os eixos
plt.figure(figsize=(12,7))
# cria o gráfico com barras horizontais
#top_10.sort_values(ascending=True).plot(kind='barh', color='green')  #skyblue
top_10.sort_values(ascending=True).plot(kind='bar', color='green')
# Adiciona titulos e labels
plt.title('Top 10 Produtos Mais Vendidos', fontsize=16)
plt.xlabel('Quantidade Vendida', fontsize=12)
plt.ylabel('Produto', fontsize=12)

#exibe o grafico
plt.tight_layout()
plt.show()
