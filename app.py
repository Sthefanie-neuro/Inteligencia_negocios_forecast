import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar as previsões
@st.cache_data
def load_data():
    df = pd.read_csv('data/forecast_all_products.csv')
    return df

df = load_data()

# Título do app
st.title("📈 Previsão de Demanda por Produto")
st.write(
    """
    Este aplicativo permite visualizar as previsões de demanda para os próximos meses.
    Selecione um produto no menu abaixo para ver o gráfico correspondente.
    """
)

# Dropdown para selecionar produto
product_list = df['StockCode'].unique()
selected_product = st.selectbox("Selecione o código do produto:", product_list)

# Filtrar dados para o produto selecionado
filtered_df = df[df['StockCode'] == selected_product]

# Gráfico interativo
fig = px.line(
    filtered_df,
    x='ds',
    y='yhat',
    labels={'ds': 'Data', 'yhat': 'Previsão de Unidades Vendidas'},
    title=f"Previsão de Demanda para o Produto {selected_product}",
    template='plotly_white'
)

# Adicionar intervalo de confiança
fig.add_traces([
    px.scatter(
        filtered_df,
        x='ds',
        y='yhat_lower',
        opacity=0
    ).data[0],
    px.scatter(
        filtered_df,
        x='ds',
        y='yhat_upper',
        opacity=0
    ).data[0]
])

fig.update_traces(mode="lines+markers")
fig.update_layout(showlegend=False)

# Exibir gráfico
st.plotly_chart(fig, use_container_width=True)

# Mostrar tabela opcional
if st.checkbox("Mostrar dados em tabela"):
    st.dataframe(filtered_df)
