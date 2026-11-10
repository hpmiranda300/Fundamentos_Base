import pandas as pd
from pathlib import Path

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df  # Return the DataFrame after loading
    
    def filtrar_por(self, coluna, atributo):        
        return self.df[self.df[coluna] == atributo]


pasta_raiz = Path(__file__).parent
arquivo_csv = pasta_raiz / 'exemplos.csv' # substitua 'exemplo.csv' pelo caminho do seu arquivo CSV

filtro = 'estado'
limite = 'SP'

processador = CsvProcessor(arquivo_csv)
processador.carregar_csv()
print (processador.filtrar_por(filtro, limite))
print(processador.df)

limite = 'DF'
processador2 = CsvProcessor(arquivo_csv)
processador2.carregar_csv()
print (processador2.filtrar_por(filtro, limite))