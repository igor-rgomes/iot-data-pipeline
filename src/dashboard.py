import os
import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)

st.set_page_config(page_title="Dashboard IoT", layout="wide")

st.title("Dashboard de Leituras de Temperatura IoT")

def carregar_dados(view):
    query = f"SELECT * FROM {view}"
    return pd.read_sql(query, engine)

# média de temperatura por sala
st.header("Média de Temperatura por Sala")

df1 = carregar_dados("avg_temp_por_room")
fig1 = px.bar(df1, x="room_id", y="avg_temp", title="Temperatura média por sala")
st.plotly_chart(fig1, use_container_width=True)

# leituras por hora
st.header("Quantidade de Leituras por Hora")

df2 = carregar_dados("leituras_por_hora")
fig2 = px.line(df2, x="hora", y="total_leituras", title="Leituras ao longo do dia")
st.plotly_chart(fig2, use_container_width=True)

# máximas e mínimas por dia
st.header("Temperatura Máxima e Mínima por Dia")

df3 = carregar_dados("temp_max_min_por_dia")
fig3 = px.line(df3, x="data", y=["temp_max", "temp_min"], title="Máx e Min por dia")
st.plotly_chart(fig3, use_container_width=True)