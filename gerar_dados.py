import pandas as pd
import random
from datetime import datetime, timedelta

# Configuração dos dados fictícios
random.seed(42)
produtos = ['Notebook', 'Smartphone', 'Teclado Mecânico', 'Monitor 4K', 'Fone Bluetooth']
categorias = ['Eletrônicos', 'Eletrônicos', 'Acessórios', 'Monitores', 'Acessórios']
prod_cat = dict(zip(produtos, categorias))

data_inicial = datetime(2026, 1, 1)
dados = []

# Gerando 500 registros de vendas
for i in range(1, 501):
    prod = random.choice(produtos)
    qtd = random.randint(1, 3)
    preco_unit = {'Notebook': 4500, 'Smartphone': 2500, 'Teclado Mecânico': 350, 'Monitor 4K': 1800, 'Fone Bluetooth': 200}[prod]
    data = data_inicial + timedelta(days=random.randint(0, 270))
    
    dados.append({
        'ID_Pedido': f'REQ{i:04d}',
        'Data': data.strftime('%Y-%m-%d'),
        'Produto': prod,
        'Categoria': prod_cat[prod],
        'Quantidade': qtd,
        'Preco_Unitario': preco_unit,
        'Total_Venda': qtd * preco_unit
    })

# Salvando a planilha em CSV
df_original = pd.DataFrame(dados)
df_original.to_csv('vendas.csv', index=False)
print("✅ Sucesso: O arquivo 'vendas.csv' foi criado na sua pasta!")
