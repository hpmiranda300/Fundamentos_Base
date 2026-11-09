from etl import pipeline_calcular_kpi_de_vendas_consolidado
from pathlib import Path

pasta_raiz: Path = Path(__file__).parent
pasta_entrada: str = pasta_raiz / 'data'
pasta_saida: str = pasta_raiz / 'output'

formato_de_saida: list = ["csv", "parquet"]

pipeline_calcular_kpi_de_vendas_consolidado(pasta_entrada, formato_de_saida, pasta_saida)
