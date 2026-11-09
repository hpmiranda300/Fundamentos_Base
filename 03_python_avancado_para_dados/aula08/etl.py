import pandas as pd
import glob
import os
import pandera as pa
from schema import VendasSchema
from pathlib import Path

@pa.check_output(VendasSchema)
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_total)
    return df_total

def transformar_dados(df: pd.DataFrame):
    df['Receita'] = df['Quantidade'] * df['Venda']
    print(df)
    return df

def carregar_dados(df: pd.DataFrame, formatos: list, pasta_saida: str):
    # Cria a pasta caso ainda não exista
    pasta = Path(pasta_saida)
    pasta.mkdir(parents=True, exist_ok=True)

    for formato in formatos:
        if formato == "csv":
            arquivo = pasta / "dados.csv"
            df.to_csv(arquivo, index=False)

        elif formato == "parquet":
            arquivo = pasta / "dados.parquet"
            df.to_parquet(arquivo, index=False)

def pipeline(pasta_entrada: str, formato_saida: list, pasta_saida: str):
    dados = extrair_dados(pasta_entrada)
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, formato_saida, pasta_saida)
    #print(pd.read_parquet('aula08/output/dados.parquet'))