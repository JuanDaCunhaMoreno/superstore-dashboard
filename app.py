import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Dashboard de Vendas e Lucro")
#Carregar o CSV
df = pd.read_csv("sample_superstore.csv")

df = df.dropna()
#Convertendo coluna Data para datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors = "coerce")
print(df.info())

#Criando colunas de análise
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

#Agrupando dados
sales_mes = df.groupby("Month")["Sales"].sum().sort_index().reset_index()
sales_anoMes = df.groupby("YearMonth")["Sales"].sum().reset_index()
profit_ano = df.groupby("Year")["Profit"].sum().sort_index().reset_index()
profit_anoMes = df.groupby("YearMonth")["Profit"].sum().reset_index()

#KPIs
st.subheader("Principais Métricas")
col1, col2, col3 = st.columns(3)
col1.metric("Faturamento Total", f"R$ {df['Sales'].sum():,.2f}")
col2.metric("Lucro Total", f"R${df['Profit'].sum():,.2f}")
col3.metric("Ticket Médio", f"R$ {(df['Sales'].sum()/df['Quantity'].sum()):,.2f}")

#Gráficos
st.subheader("Lucro por Ano")
fig1, ax1 = plt.subplots()
sns.lineplot(data=profit_ano, x = "Year", y = "Profit", ax = ax1)
ax1.grid(True)
st.pyplot(fig1)

st.subheader("Lucro Mensal")
fig2, ax2 = plt.subplots(figsize = (20 ,5))
sns.lineplot(data=profit_anoMes, x = "YearMonth", y = "Profit", marker = "o", ax = ax2)
plt.xticks(rotation=45)
ax2.grid(True)
st.pyplot(fig2)

st.subheader("Faturamento por Mês")
fig3, ax3 = plt.subplots()
sns.lineplot(data=sales_mes, x = "Month", y = "Sales", ax = ax3)
ax3.grid(True)
st.pyplot(fig3)

st.subheader("Faturamento Mensal")
fig4, ax4 = plt.subplots(figsize = (20 ,5))
sns.lineplot(data=sales_anoMes, x = "YearMonth", y = "Sales", marker = "o", ax = ax4)
plt.xticks(rotation=45)
ax4.grid(True)
st.pyplot(fig4)
