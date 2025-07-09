#Módulo 1: Análise exploratória e painel de vendas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/DELL/Downloads/dados_retail/online_retail.csv")
print(df.head())

# Limpeza básica
df.dropna(subset=['CustomerID'], inplace=True)  # Remove linhas sem cliente
df = df[df['Quantity'] > 0]                     # Remove devoluções
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])  # Converter datas

# Criar coluna de receita
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Agrupar receita por mês
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()

# Plotar receita mensal
plt.figure(figsize=(10,5))
monthly_revenue.plot(kind='bar', color='teal')
plt.title('Receita Mensal')
plt.ylabel('Receita (£)')
plt.xlabel('Mês')
plt.show()

# Agrupar por produto
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

# Plotar
top_products.plot(kind='barh', color='coral', figsize=(8,5))
plt.title('Top 10 Produtos Mais Vendidos')
plt.xlabel('Quantidade Vendida')
plt.gca().invert_yaxis()
plt.show()

# Agrupar receita por cliente
top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)

# Plotar
top_customers.plot(kind='bar', color='purple', figsize=(8,5))
plt.title('Top 10 Clientes (Receita Gerada)')
plt.ylabel('Receita (£)')
plt.xlabel('ID do Cliente')
plt.show()

# Receita por país
country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)

# Plotar
country_revenue.plot(kind='bar', color='green', figsize=(8,5))
plt.title('Receita por País (Top 10)')
plt.ylabel('Receita (£)')
plt.xlabel('País')
plt.show()
