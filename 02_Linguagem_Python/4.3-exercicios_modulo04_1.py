#Exercício 1 – Exibindo uma mensagem

#Crie uma função chamada exibir_boas_vindas() que exiba a mensagem: Bem-vindo ao sistema!
#Depois, chame a função para executar a mensagem.

#Requisitos:

#Utilize def.
#A função não deve receber parâmetros.
#A função não precisa retornar nenhum valor.

def exibir_boas_vindas() -> None:
    """Exibe uma mensagem de boas-vindas."""
    print("Bem-vindo ao sistema!")

exibir_boas_vindas()


#Exercício 2 – Identificando um produto

#Crie uma função chamada exibir_produto() que receba:
#o nome de um produto;
#o preço do produto.

#A função deve exibir uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00

#Depois, chame a função passando um produto e um preço como argumentos.

#Requisitos:
#Utilize parâmetros.
#Adicione type hints nos parâmetros.
#A função deve retornar None.

def exibir_produto(nome_produto: str, preco_produto: float) -> None:
    """Exibe uma mensagem com o nome e o preço do produto.
    
    Args:
        nome_produto (str): Nome do produto.
        preco_produto (float): Preço do produto.
    """
    print(f"Produto: {nome_produto} | Preço: R$ {preco_produto:.2f}")

exibir_produto("Teclado", 150.00)


#Exercício 3 – Calculando o valor de uma compra

#Crie uma função chamada calcular_total() que receba:
#o preço de um produto;
#a quantidade comprada.

#A função deve calcular e retornar o valor total da compra.

#Exemplo:

#total = calcular_total(50.0, 3)
#print(total)

#Resultado esperado: 150.0

#Requisitos:
#preco deve possuir type hint float.
#quantidade deve possuir type hint int.
#A função deve indicar que retorna um float.
#Utilize return para devolver o resultado.


def calcular_total(preco: float, quantidade: int) -> float:
    """Calcula o valor total da compra.
    
    Args:
        preco (float): Preço do produto.
        quantidade (int): Quantidade comprada.
        
    Returns:
        float: Valor total da compra.   
    """
    return preco * quantidade

total = calcular_total(50.0, 3)
print(total)



#Exercício 4 – Calculando a média de avaliações

#Uma plataforma armazena três avaliações dadas por usuários para um produto.

#Crie uma função chamada calcular_media_avaliacoes() que receba três notas e retorne a média entre elas.

#Depois, utilize o resultado retornado pela função para exibir a média das avaliações

#Requisitos:

#Utilize parâmetros e argumentos.
#Adicione type hints.
#Utilize return.
#Adicione uma docstring explicando o que a função recebe e o que retorna.
#Guarde o resultado da função em uma variável antes de exibi-lo.


def calcular_media_avaliacoes(nota1: float, nota2: float, nota3: float) -> float:
    """Calcula a média de três avaliações.
    
    Args:
        nota1 (float): Primeira avaliação.
        nota2 (float): Segunda avaliação.
        nota3 (float): Terceira avaliação.
        
    Returns:
        float: Média das avaliações.   
    """
    return (nota1 + nota2 + nota3) / 3

media_avaliacoes = calcular_media_avaliacoes(7.5, 8.0, 6.5)
print(f"Media das avaliações: {media_avaliacoes:.2f}")


#Exercício 5 – Processando um pedido
#
#Você precisa criar duas funções para representar uma pequena parte de um sistema de pedidos.
#
#A primeira função deve se chamar: calcular_valor_final()
#
#Ela deve receber:
#
#preço unitário;
#quantidade;
#desconto em formato decimal.
#Por exemplo, 0.10 representa 10% de desconto.
#
#A função deve calcular e retornar o valor final do pedido após o desconto.
#
#Depois, crie uma segunda função chamada: exibir_resumo_pedido()
#
#Ela deve receber:
#número do pedido;
#valor final.
#
#E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00
#
#Requisitos:
#As duas funções devem possuir type hints.
#calcular_valor_final() deve retornar um float.
#exibir_resumo_pedido() deve retornar None.
#As duas funções devem possuir docstrings.
#O valor retornado por calcular_valor_final() deve ser passado como argumento para exibir_resumo_pedido().
#Não faça o cálculo diretamente fora da função.


def calcular_valor_final(preco_unitario: float, quantidade: int, desconto: float) -> float:
    """Calcula o valor final do pedido após o desconto.
    
    Args:
        preco_unitario (float): Preço unitário do produto.
        quantidade (int): Quantidade de produtos.
        desconto (float): Desconto em formato decimal.
        
    Returns:
        float: Valor final do pedido após o desconto.   
    """
    subtotal: float = preco_unitario * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto
    return total

def exibir_resumo_pedido(numero_pedido: int, valor_final: float) -> None:
    """Exibe o resumo do pedido.
    
    Args:
        numero_pedido (int): Número do pedido.
        valor_final (float): Valor final do pedido.   
    """
    print(f"Pedido #{numero_pedido} finalizado. Total: R$ {valor_final:.2f}")


valor_final = calcular_valor_final(
    preco_unitario=90.00,
    quantidade=3,
    desconto=0.10
)

numero_pedido: int = 1058
exibir_resumo_pedido(numero_pedido, valor_final)




#Exercício 6 – Convertendo temperatura
#
#Crie uma função chamada converter_celsius_para_fahrenheit().
#
#A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.
#
#Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32
#
#Depois, armazene o resultado em uma variável e imprima a temperatura convertida.
#
#Requisitos:
#
#Receba a temperatura por parâmetro.
#Utilize type hint float.
#A função deve retornar um float.
#Utilize return.
#Adicione uma docstring explicando a função.


def converter_celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit.
    
    Args:
        celsius (float): Temperatura em Celsius.
        
    Returns:
        float: Temperatura em Fahrenheit.   
    """
    fahrenheit: float = (celsius * 9 / 5) + 32
    return fahrenheit

temperatura_celsius: float = 25.0
temperatura_fahrenheit: float = converter_celsius_para_fahrenheit(temperatura_celsius)
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f}")


#Exercício 7 – Calculando consumo médio
#
#Um veículo percorreu determinada distância utilizando uma quantidade de combustível.
#
#Crie uma função chamada calcular_consumo_medio() que receba:
#
#distância percorrida em quilômetros;
#quantidade de litros utilizados.
#
#A função deve retornar quantos quilômetros o veículo percorreu por litro.
#
#Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
#Resultado: 12.0
#
#Depois, crie uma segunda função chamada exibir_consumo() que receba o resultado e exiba: Consumo médio: {resultado} km/l
#
#Requisitos:
#As duas funções devem possuir type hints.
#calcular_consumo_medio() deve retornar float.
#exibir_consumo() deve retornar None.
#As duas funções devem possuir docstrings.
#O resultado da primeira função deve ser passado como argumento para a segunda.


def calcular_consumo_medio(distancia: float, litros: float) -> float:
    """Calcula o consumo médio de um veículo.
    
    Args:
        distancia (float): Distância percorrida em quilômetros.
        litros (float): Quantidade de litros utilizados.
    Returns:
        float: Consumo médio do veículo.  
    """
    return distancia / litros

def exibir_consumo(consumo: float) -> None:
    """Exibe o consumo médio de um veículo.
    
    Args:        
        consumo (float): Consumo médio do veículo.  
    """
    print(f"Consumo médio: {consumo} km/l")


consumo: float = calcular_consumo_medio(420.0, 35.0)
exibir_consumo(consumo)



#Exercício 8 – Verificando uma meta de vendas
#
#Crie uma função chamada calcular_percentual_meta() que receba:
#valor da meta;
#valor vendido.
#
#A função deve calcular e retornar o percentual da meta que foi atingido.
#
#Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
#Resultado: 75.0
#
#Depois, crie uma função chamada exibir_status_meta() que receba esse percentual.
#
#Ela deve exibir: Meta atingida!
#caso o percentual seja maior ou igual a 100.
#
#Caso contrário, deve exibir: Meta ainda não atingida.
#
#Requisitos:
#Utilize type hints.
#calcular_percentual_meta() deve retornar float.
#exibir_status_meta() deve retornar None.
#Utilize o valor retornado por uma função como argumento da outra.
#Adicione docstrings nas duas funções.
#Não repita o cálculo do percentual fora da função.

def calcular_percentual_meta(meta: float, valor_vendido: float) -> float:
    """Calcula o percentual da meta que foi atingido.
    
    Args:
        meta (float): Valor da meta.
        valor_vendido (float): Valor vendido.
    Returns:
        float: Percentual da meta atingido.   
    """
    return (valor_vendido / meta) * 100

def exibir_status_meta(percentual: float) -> None:
    """Exibe o status da meta.
    
    Args:        
        percentual (float): Percentual da meta atingido.  
    """
    if percentual >= 100:
        print("Meta atingida!")
    else:
        print("Meta ainda não atingida.")


percentual: float = calcular_percentual_meta(10000.0, 7500.0)
exibir_status_meta(percentual)



#Exercício 9 – Analisando uma entrega
#
#Você está desenvolvendo uma pequena parte de um sistema de entregas.
#
#Crie uma função chamada calcular_tempo_estimado() que receba:
#
#distância da entrega em quilômetros;
#velocidade média do veículo em km/h.
#
#A função deve calcular e retornar o tempo estimado da entrega em horas.
#
#Use: tempo = distancia / velocidade
#
#Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:
#
#"Entrega rápida" se o tempo for menor ou igual a 1;
#"Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
#"Entrega demorada" se o tempo for maior que 3.
#
#Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:
#o tempo estimado;
#a classificação.
#
#Ela deve exibir algo como:
#Tempo estimado: 2.5 horas
#Classificação: Entrega normal
#
#
#Requisitos:
#As três funções devem possuir type hints.
#calcular_tempo_estimado() deve retornar float.
#classificar_entrega() deve retornar str.
#exibir_resumo_entrega() deve retornar None.
#Todas devem possuir docstrings.
#O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
#Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
#Cada função deve possuir apenas uma responsabilidade.


def calcular_tempo_estimado(distancia: float, velocidade: float) -> float:
    """Calcula o tempo estimado de uma entrega.
    
    Args:
        distancia (float): Distância da entrega em quilômetros.
        velocidade (float): Velocidade média do veículo em km/h.  
    Returns:
        float: Tempo estimado da entrega em horas.  
    """
    return distancia / velocidade


def classificar_entrega(tempo_estimado: float) -> str:
    """Classifica o tempo estimado de uma entrega.
    
    Args:        
        tempo_estimado (float): Tempo estimado da entrega em horas.  
    Returns:
        str: Classificação da entrega.  
    """
    if tempo_estimado <= 1:
        return "Entrega rápida"
    elif tempo_estimado <= 3:
        return "Entrega normal"
    else:
        return "Entrega demorada"


def exibir_resumo_entrega(tempo_estimado: float, classificacao_entrega: str) -> None:
    """Exibe o resumo da entrega.
    
    Args:        
        tempo_estimado (float): Tempo estimado da entrega em horas.  
        classificacao_entrega (str): Classificação da entrega.  
    """
    print(f"Tempo estimado: {tempo_estimado:.2f} horas")
    print(f"Classificação: {classificacao_entrega}")


distancia: float = 360
velocidade: float = 80
tempo_estimado: float = calcular_tempo_estimado(distancia, velocidade)

classificacao_entrega: str = classificar_entrega(tempo_estimado)

exibir_resumo_entrega(tempo_estimado, classificacao_entrega)



#Exercício 10 – Sistema de Aprovação de Empréstimo
#
#Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.
#
#O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.
#
#1. Calcular comprometimento da renda
#Crie uma função chamada calcular_comprometimento_renda() que receba:
#
#renda mensal;
#valor da parcela do empréstimo.
#Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.
#
#Use:
#
#percentual = (parcela / renda) * 100
#
#A função deve retornar esse percentual.
#
#2. Analisar o empréstimo
#Crie uma segunda função chamada analisar_emprestimo() que receba:
#
#renda mensal;
#valor solicitado;
#percentual de comprometimento da renda.
#A função deve retornar uma das seguintes classificações:
#
#"Aprovado"
#"Análise manual"
#"Recusado"
#
#Utilize estas regras:
#
#Se o comprometimento da renda for maior que 40%, retorne "Recusado".
#Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
#Caso contrário, retorne "Aprovado".
#
#
#3. Calcular o total do pagamento
#Crie uma terceira função chamada calcular_total_pagamento() que receba:
#
#valor da parcela;
#quantidade de parcelas.
#Ela deve retornar o valor total que será pago ao final do empréstimo.
#
#Exemplo:
#
#Parcela: R$ 850.00
#Quantidade: 24
#
#Total pago: R$ 20400.00
#
#4. Exibir o resultado final
#Por fim, crie uma função chamada exibir_resultado() que receba:
#
#valor solicitado;
#percentual de comprometimento;
#total que será pago;
#resultado da análise.
#Ela deve apenas exibir um resumo como:
#
#--- Análise do empréstimo ---
#
#Valor solicitado: R$ 15000.00
#Comprometimento da renda: 28.3%
#Total a pagar: R$ 20400.00
#
#Resultado: Aprovado
#
#
#Essa função não deve retornar nenhuma informação.
#
#
#
#Requisitos
#Todas as funções devem possuir type hints.
#Todas devem possuir docstrings.
#calcular_comprometimento_renda() deve retornar float.
#analisar_emprestimo() deve retornar str.
#calcular_total_pagamento() deve retornar float.
#exibir_resultado() deve retornar None.
#Os cálculos devem acontecer dentro das funções responsáveis por eles.
#Não repita cálculos fora das funções.
#Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
#A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
#Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.
#
#Fluxo esperado
#
#dados do empréstimo
#↓
#calcular comprometimento da renda
#↓
#analisar empréstimo
#↓
#calcular total do pagamento
#↓
#exibir resultado final
#
#
#O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.



def calcular_comprometimento_renda(renda_mensal: float, valor_parcela: float) -> float:
    """Calcula o percentual de comprometimento da renda mensal.
    
    Args:
        renda_mensal (float): Renda mensal do solicitante.
        valor_parcela (float): Valor da parcela do empréstimo.
    Returns:
        float: Percentual de comprometimento da renda mensal.
    """
    return (valor_parcela / renda_mensal) * 100


def analisar_emprestimo(renda_mensal: float, valor_solicitado: float, percentual_comprometimento: float) -> str:
    """Analisa o empréstimo e retorna uma classificação.
    
    Args:
        renda_mensal (float): Renda mensal do solicitante.
        valor_solicitado (float): Valor solicitado no empréstimo.
        percentual_comprometimento (float): Percentual de comprometimento da renda mensal.
    Returns:
        str: Classificação do empréstimo.
    """
    if percentual_comprometimento > 40:
        return "Recusado"
    elif (valor_solicitado > (renda_mensal * 5)):
        return "Análise manual"
    else:
        return "Aprovado"


def calcular_total_pagamento(valor_parcela: float, quantidade_parcelas: int) -> float:
    """Calcula o valor total do pagamento.
    
    Args:
        valor_parcela (float): Valor da parcela do empréstimo.
        quantidade_parcelas (int): Quantidade de parcelas.
    Returns:
        float: Valor total do pagamento.
    """
    return valor_parcela * quantidade_parcelas


def exibir_resultado(
    valor_solicitado: float,
    percentual_comprometimento: float,
    total_pagamento: float,
    resultado_analise: str
) -> None:
    """Exibe o resultado da análise do empréstimo.
    
    Args:
        valor_solicitado (float): Valor solicitado no empréstimo.
        percentual_comprometimento (float): Percentual de comprometimento da renda mensal.
        total_pagamento (float): Valor total do pagamento.
        resultado_analise (str): Classificação do empréstimo.
    """
    print("--- Análise do empréstimo ---")
    print(f"Valor solicitado: R$ {valor_solicitado:.2f}")
    print(f"Comprometimento da renda: {percentual_comprometimento:.1f}%")
    print(f"Total a pagar: R$ {total_pagamento:.2f}")
    print(f"Resultado: {resultado_analise}")


#dados do empréstimo
renda_mensal: float = 4000
valor_parcela: float = 1500
percentual_comprometimento: float = 0

#calcular comprometimento da renda
percentual_comprometimento=calcular_comprometimento_renda (renda_mensal, valor_parcela)

#analisar empréstimo
valor_solicitado: float = 50000
quantidade_parcelas: int = 24
resultado_analise: str = ""
resultado_analise=analisar_emprestimo(renda_mensal, valor_solicitado, percentual_comprometimento)

#calcular total do pagamento
total_pagamento: float = 0
total_pagamento=calcular_total_pagamento(valor_parcela, quantidade_parcelas)

#exibir resultado final
exibir_resultado(valor_solicitado, percentual_comprometimento, total_pagamento, resultado_analise)
