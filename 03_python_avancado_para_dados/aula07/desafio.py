import csv

# Função para ler o arquivo CSV
def ler_csv(nome_arquivo: str) -> list:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

# Função para processar os dados em um dicionário
#dados_bruto [
# {'Produto': 'Notebook', 'Categoria': 'Electronics', 'Quantidade': '5', 'Venda': '3000'}, 
# {'Produto': 'Smartphone', 'Categoria': 'Electronics', 'Quantidade': '10', 'Venda': '500'}, 
# {'Produto': 'Camiseta', 'Categoria': 'Apparel', 'Quantidade': '20', 'Venda': '20'}, 
# {'Produto': 'Cafeteira', 'Categoria': 'Kitchen', 'Quantidade': '3', 'Venda': '100'}, 
# {'Produto': 'Tênis', 'Categoria': 'Apparel', 'Quantidade': '10', 'Venda': '50'}, 
# {'Produto': 'Tablet', 'Categoria': 'Electronics', 'Quantidade': '2', 'Venda': '1500'}
#]
def processar_dados(dados: list) -> dict:
    vendas_por_categoria = {}

    for item in dados:
        categoria = item['Categoria']
        quantidade = int(item['Quantidade'])
        venda = float(item['Venda'])
        faturamento = quantidade * venda

        #O if garante que a lista seja criada apenas na primeira ocorrência da categoria.
        if categoria not in vendas_por_categoria:
            #cria uma lista para cada categoria.
            vendas_por_categoria[categoria] = []

        #adiciona o faturamento de cada produto à lista correspondente.
        vendas_por_categoria[categoria].append(faturamento)

    return vendas_por_categoria


def processar_dados1(dados: list) -> dict:
    vendas_por_categoria = {}

    for item in dados:
        categoria = item['Categoria']
        quantidade = int(item['Quantidade'])
        venda = float(item['Venda'])
        faturamento = quantidade * venda

        # Obtém a lista existente ou cria uma lista vazia.
        #Se a categoria já existir, retorna a lista existente.
        #Se a categoria não existir, retorna uma lista vazia [].
        vendas_por_categoria[categoria] = vendas_por_categoria.get(categoria, [])

        # Adiciona o faturamento à lista da categoria.
        vendas_por_categoria[categoria].append(faturamento)

    return vendas_por_categoria    

def processar_dados2(dados: list) -> dict:    
    vendas_por_categoria = {}

    for item in dados:
        categoria = item['Categoria']
        quantidade = int(item['Quantidade'])
        venda = float(item['Venda'])

        faturamento = quantidade * venda

        #Minha recomendação: use setdefault() nesse caso. Ele foi criado justamente para facilitar esse tipo de operação: 
        # criar uma chave com um valor padrão caso ela ainda não exista e utilizar esse valor.
        #É uma forma bastante elegante de trabalhar com dicionários e listas em Python!
        vendas_por_categoria.setdefault(categoria, []).append(faturamento)

    return vendas_por_categoria


# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(dados: dict) -> dict:
    total_por_categoria = {}

    #.items() percorre as categorias e suas respectivas listas.
    for categoria, vendas in dados.items():
        #sum(vendas) soma todos os valores da lista.
        #O resultado é armazenado no dicionário total_por_categoria.
        total_por_categoria[categoria] = sum(vendas)

    return total_por_categoria

def calcular_vendas_categoria1(dados: dict) -> dict:
    #Dica: você também pode fazer isso em uma única linha usando Dictionary Comprehension:
    total_por_categoria = { categoria: sum(vendas) for categoria, vendas in dados.items() }
    return total_por_categoria


# Função principal para integrar as funções anteriores
def main():
    nome_arquivo: str = 'aula07/vendas.csv'
    dados_brutos: list = ler_csv(nome_arquivo)
    dados_processados: dict = processar_dados2(dados_brutos)    
    vendas_categoria: dict = calcular_vendas_categoria(dados_processados)    
    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()