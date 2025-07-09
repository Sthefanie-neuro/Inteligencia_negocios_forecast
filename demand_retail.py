# Previsão de Demanda para TODOS os Produtos

# Importação de bibliotecas
import pandas as pd
from prophet import Prophet
from tqdm import tqdm  # Barra de progresso
import os

# Carregar dataset
df = pd.read_csv("C:/Users/DELL/Downloads/dados_retail/online_retail.csv")

# Limpeza básica de dados
df.dropna(subset=['CustomerID'], inplace=True)  # Remove linhas sem cliente
df = df[df['Quantity'] > 0]                      # Remove devoluções
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])  # Converter datas

# Criar coluna de receita
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Obter lista de produtos únicos
products = df['StockCode'].unique()

# Lista para armazenar resultados
all_forecasts = []

# Iterar sobre cada produto
for product in tqdm(products, desc="Gerando previsões"):
    # Filtrar dados do produto
    product_sales = (
        df[df['StockCode'] == product]
        .groupby(df['InvoiceDate'].dt.to_period('M'))['Quantity']
        .sum()
        .reset_index()
    )
    
    # Ignorar produtos com poucos dados
    if len(product_sales) < 6:
        continue
    
    # Preparar dados para o Prophet
    product_sales['InvoiceDate'] = product_sales['InvoiceDate'].dt.to_timestamp()
    product_sales.rename(columns={'InvoiceDate': 'ds', 'Quantity': 'y'}, inplace=True)
    
    try:
        # Criar e treinar modelo Prophet
        model = Prophet()
        model.fit(product_sales)
        
        # Criar dataframe futuro para 6 meses
        future = model.make_future_dataframe(periods=6, freq='M')
        
        # Fazer previsões
        forecast = model.predict(future)
        
        # Adicionar coluna com o código do produto
        forecast['StockCode'] = product
        
        # Selecionar apenas as colunas relevantes
        forecast = forecast[['StockCode', 'ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        
        # Adicionar ao conjunto de previsões
        all_forecasts.append(forecast)
    
    except Exception as e:
        print(f"Erro ao processar produto {product}: {e}")

# Concatenar todas as previsões
final_forecast = pd.concat(all_forecasts, ignore_index=True)


os.makedirs("data", exist_ok=True)

# Salvar em CSV
final_forecast.to_csv('data/forecast_all_products.csv', index=False)

print("✅ Previsões para todos os produtos salvas em 'forecast_all_products.csv'")
