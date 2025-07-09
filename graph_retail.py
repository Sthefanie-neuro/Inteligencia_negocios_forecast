#Gráfico Interativo: Previsão de Demanda com Dropdown

import pandas as pd
import plotly.express as px

# Carregar as previsões já geradas para todos os produtos
forecast_df = pd.read_csv('data/forecast_all_products.csv')

# Filtrar apenas os próximos 6 meses (se necessário)
# forecast_df = forecast_df[forecast_df['ds'] >= '2023-01-01']

# Gráfico interativo
fig = px.line(
    forecast_df,
    x='ds',
    y='yhat',
    color='StockCode',
    title='Previsão de Demanda por Produto',
    labels={'ds': 'Data', 'yhat': 'Previsão de Unidades Vendidas', 'StockCode': 'Produto'},
    template='plotly_white'
)

# Adicionar dropdown para seleção do produto
fig.update_layout(
    updatemenus=[
        {
            "buttons": [
                {
                    "method": "update",
                    "label": product,
                    "args": [{"visible": [code == product for code in forecast_df['StockCode'].unique()]},
                             {"title": f"Previsão de Demanda - Produto {product}"}]
                }
                for product in forecast_df['StockCode'].unique()
            ],
            "direction": "down",
            "showactive": True,
        }
    ]
)

# Mostrar gráfico
fig.show()
