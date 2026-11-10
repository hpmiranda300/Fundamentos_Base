import pandas as pd
from pathlib import Path

pasta_raiz = Path(__file__).parent
arquivo_csv = pasta_raiz / 'exemplos.csv' # substitua 'exemplo.csv' pelo caminho do seu arquivo CSV

df = pd.read_csv(arquivo_csv)

df_filtrado = df[df['estado'] == 'SP']

df_filtrado = df[df['preço'] == '10,50']


print(df_filtrado)



df2 = pd.read_csv(arquivo_csv)

df_filtrado2 = df2[df2['estado'] == 'DF']

#df_filtrado2 = df2[df2['preço'] == '10,50']

print(df_filtrado2)