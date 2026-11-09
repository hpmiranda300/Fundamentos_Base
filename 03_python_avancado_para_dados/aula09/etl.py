import pandas as pd
import os
import glob
from decorator_hudson import log_decorator, time_measure_decorator
from pathlib import Path

# uma funcao de extract que le e consolida os json
@log_decorator
@time_measure_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma funcao que transforma
@log_decorator
@time_measure_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
@time_measure_decorator
#carregar_dados(data_frame_calculado, formato_de_saida, pasta_saida)
def carregar_dados(df: pd.DataFrame, format_saida: list, pasta_saida: str):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    # Cria a pasta caso ainda não exista
    pasta = Path(pasta_saida)
    pasta.mkdir(parents=True, exist_ok=True)
    for formato in format_saida:
        if formato == 'csv':
            arquivo = pasta / "dados.csv"
            df.to_csv(arquivo, index=False)            
        if formato == 'parquet':
            arquivo = pasta / "dados.parquet"
            df.to_parquet(arquivo, index=False)            


@log_decorator
@time_measure_decorator
#pipeline_calcular_kpi_de_vendas_consolidado(pasta_entrada, formato_de_saida, pasta_saida)
def pipeline_calcular_kpi_de_vendas_consolidado(pasta_entrada: str, formato_de_saida: list, pasta_saida: str):
    data_frame = extrair_dados_e_consolidar(pasta_entrada)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida, pasta_saida)

# uma funcao que da load em csv ou parquet    
print(carregar_dados.__doc__)