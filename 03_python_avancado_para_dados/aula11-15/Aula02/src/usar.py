from interface.classes.csv_class import CsvProcessor
from pathlib import Path
# import pandas as pd

pasta_raiz = Path(__file__).parent
arquivo_csv = pasta_raiz / 'exemplos.csv' # substitua 'exemplo.csv' pelo caminho do seu arquivo CSV

filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()  # Load the CSV
print(arquivo_CSV.filtrar_por(['estado', 'preço'], ['SP', '10,50']))
# print(arquivo_CSV.df)
print("#########################")
# arquivo_csv2 = './examplo2.csv'
# filtro2 = 'estado'  # Changed to filtro2
# limite2 = 'DF'

# arquivo_CSV2 = CsvProcessor(arquivo_csv2)
# arquivo_CSV2.carregar_csv()  # Load the CSV
# print(arquivo_CSV2.filtrar_por(filtro2, limite2))  # Changed to filtro2
# print(arquivo_CSV2.sub_filtro('preço', '10,50'))
