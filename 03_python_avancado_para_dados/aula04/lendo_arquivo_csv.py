#3.Lendo arquivos
#Para ler um arquivo CSV em Python utilizando o módulo nativo, você pode usar a combinação do comando with open... para abrir o arquivo 
#e o método .reader() do módulo csv para ler o arquivo linha por linha. 
# O uso de with assegura que o arquivo será fechado corretamente após sua leitura, mesmo que ocorram erros durante o processo. 
# Abaixo está um exemplo básico de como realizar essa operação:

import csv

# Caminho para o arquivo CSV
caminho_arquivo = 'aula04\exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)    