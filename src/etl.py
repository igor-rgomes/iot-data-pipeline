import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# carregar variáveis do .env
load_dotenv()

def main():

    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)

    print("Conectando ao banco...")

    # ler CSV
    arquivo = "data/IOT-temp.csv"
    df = pd.read_csv(arquivo)

    print("Colunas encontradas:")
    print(df.columns)

    # padronizar colunas
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # converter tipos
    if "noted_date" in df.columns:
        df["noted_date"] = pd.to_datetime(df["noted_date"], errors="coerce")

    if "temp" in df.columns:
        df["temp"] = pd.to_numeric(df["temp"], errors="coerce")

    # remover linhas inválidas
    df = df.dropna()

    print("Inserindo dados no PostgreSQL...")

    df.to_sql(
        "temperature_readings",
        engine,
        if_exists="replace",
        index=False
    )

    print("ETL finalizado com sucesso!")
    print(df.head())


if __name__ == "__main__":
    main()