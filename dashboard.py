
import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine

# Função para conectar ao banco de dados
def load_data():
    engine = create_engine('mssql+pyodbc://username:password@server/database?driver=SQL+Server')
    query = """
    SELECT 
        soh.OrderDate,
        soh.TotalDue,
        a.StateProvinceID AS Region,
        p.Name AS Product
    FROM 
        Sales.SalesOrderHeader soh
    JOIN 
        Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
    JOIN 
        Person.Address a ON soh.ShipToAddressID = a.AddressID
    JOIN 
        Production.Product p ON sod.ProductID = p.ProductID;
    """
    return pd.read_sql(query, engine)

# Carregar os dados
df = load_data()

# Processar e manipular os dados
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Ano'] = df['OrderDate'].dt.year
df['Mês'] = df['OrderDate'].dt.month

# Configurar o layout do Streamlit
st.title('Dashboard de Vendas - AdventureWorks')

# Filtros
selected_region = st.multiselect('Selecione a Região', options=df['Region'].unique())
selected_product = st.multiselect('Selecione o Produto', options=df['Product'].unique())
date_range = st.date_input("Selecione o intervalo de datas", [])

# Filtrar dados
filtered_data = df
if selected_region:
    filtered_data = filtered_data[filtered_data['Region'].isin(selected_region)]
if selected_product:
    filtered_data = filtered_data[filtered_data['Product'].isin(selected_product)]
if date_range:
    filtered_data = filtered_data[(filtered_data['OrderDate'] >= date_range[0]) & (filtered_data['OrderDate'] <= date_range[1])]

# KPI
total_vendas = filtered_data['TotalDue'].sum()
st.metric(label="Total de Vendas", value=f"R$ {total_vendas:,.2f}")

# Gráfico de barras - Vendas por Produto
vendas_por_produto = filtered_data.groupby('Product')['TotalDue'].sum().reset_index()
fig_produto = px.bar(vendas_por_produto, x='Product', y='TotalDue',
                     title='Vendas por Produto', labels={'TotalDue': 'Total de Vendas', 'Product': 'Produto'})
st.plotly_chart(fig_produto)

# Gráfico de linhas - Vendas ao longo do Tempo
vendas_por_tempo = filtered_data.groupby(['Ano', 'Mês'])['TotalDue'].sum().reset_index()
fig_tempo = px.line(vendas_por_tempo, x='Mês', y='TotalDue', color='Ano',
                    title='Vendas ao longo do Tempo', labels={'TotalDue': 'Total de Vendas', 'Mês': 'Mês'})
st.plotly_chart(fig_tempo)
