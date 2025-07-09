# Inteligência de Negócios com IA

Este projeto utiliza **Inteligência Artificial e Visualização de Dados** para análise exploratória, previsão de demanda e criação de painéis interativos com **Python**. Ele foi desenvolvido como parte do meu portfólio em Ciência de Dados.

---

## Funcionalidades

✅ **Módulo 1: Análise Exploratória e Painel de Vendas**  
- Limpeza e análise de dados do varejo online.  
- Geração de indicadores (vendas totais, produtos mais vendidos, receita por país).  
- Criação de painéis interativos com **Plotly** e **Streamlit**.  

✅ **Módulo 2: Previsão de Demanda**  
- Modelagem preditiva usando séries temporais para prever a demanda de todos os produtos.  
- Exportação das previsões para um arquivo `forecast_all_products.csv`.  

✅ **Módulo 3: Visualização Interativa com Dropdown**  
- Gráficos interativos para seleção de produtos e visualização das previsões.  

✅ **Aplicação Web com Streamlit**  
- Interface amigável para explorar os dados e previsões diretamente no navegador.  

---

## Estrutura do Repositório

```text
Inteligencia_negocios_IA/
│
├── app.py                   # Aplicação principal em Streamlit
├── online_retail.py         # Módulo 1: análise exploratória
├── demand_retail.py         # Módulo 2: previsão de demanda
├── graphs_retail.py         # Módulo 3: gráficos interativos
├── requirements.txt         # Dependências do projeto
├── data/
│   └── forecast_all_products.csv  # Previsões geradas
└── README.md                # Documentação


