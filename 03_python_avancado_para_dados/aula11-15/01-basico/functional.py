import pandas as pd
from pathlib import Path

def carregar_csv_e_filtrar(arquivo_csv, estado):
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(arquivo_csv)
    
    # Verificar e remover células vazias
    df = df.dropna()
    
    # Filtrar as linhas pela coluna estado
    df_filtrado = df[df['estado'] == estado]
    
    return df_filtrado

# Exemplo de uso
pasta_raiz = Path(__file__).parent
arquivo_csv = pasta_raiz / 'vendas.csv'

estado_filtrado = 'SP'  # estado que você quer filtrar
df_filtrado = carregar_csv_e_filtrar(arquivo_csv, estado_filtrado)

print(df_filtrado)
