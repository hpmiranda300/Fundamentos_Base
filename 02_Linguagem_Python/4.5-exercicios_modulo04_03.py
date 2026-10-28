#Exercício 14 – Unpacking com * e retorno
#
#Considere a seguinte lista:
#
#times = ["Brasil", "Argentina"]
#Crie uma função chamada montar_confronto que receba dois parâmetros:
#
#time_a
#time_b
#
#A função deve:
#
#Utilizar type hints nos parâmetros e no retorno.
#Possuir uma docstring explicando o que ela faz.
#Retornar uma string no formato Brasil x Argentina.
#Depois, chame a função desempacotando a lista com *.
#
#Você não deve acessar os valores manualmente com:
#
#times[0]
#times[1]
#
#
#Exemplo esperado de uso:
#
#confronto = montar_confronto(*times)
#print(confronto)


def montar_confronto(time_a: str, time_b: str)->str:
    """Monta o confronto entre dois times"""
    return f"{time_a} x {time_b}"


times = ["Brasil", "Argentina"]

confronto = montar_confronto(*times)
print(confronto)


#Exercício 15 – Unpacking com * e valores padrão
#
#Crie uma função chamada calcular_media com os seguintes parâmetros:
#
#nota1
#nota2
#nota3
#bonus=0
#
#A função deve:
#
#Utilizar type hints em todos os parâmetros e no retorno.
#Possuir uma docstring.
#Calcular a média das três notas.
#Somar o valor de bonus ao resultado final.
#Retornar a média calculada.
#Considere:
#
#notas = [8.5, 7.0, 9.5]
#
#Chame a função utilizando * para desempacotar as notas:
#
#resultado = calcular_media(*notas)
#print(resultado)
#
#Depois, faça uma segunda chamada utilizando a mesma lista, mas informe bonus como argumento nomeado.
#
#Por fim, altere a lista para possuir quatro notas:
#
#notas = [8.5, 7.0, 9.5, 10.0]
#
#Tente realizar novamente:
#
#calcular_media(*notas)
#
#Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.

def calcular_media(nota1:float, nota2:float, nota3:float, bonus:float =0) -> float:
    """Calcula a média das notas e soma o bônus"""
    return ((nota1 + nota2 + nota3) / 3) + bonus

notas = [8.5, 7.0, 9.5]
resultado1 = calcular_media(*notas)
print(f"Média sem bonus informado: {resultado1}")

resultado2 = calcular_media(*notas, bonus=1)
print(f"Média com bônus de 1: {resultado2}")

notas2 = [8.5, 7.0, 9.5, 10.0]
resultado3 = calcular_media(*notas2)
print(f"Média com 4 notas sem bônus informado: {resultado3}")

"""
O quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus porque a função foi definida para receber apenas três 
notas e um parâmetro bônus com valor padrão 0. Quando mais de três valores são passados, o Python tenta encaixá-los nos parâmetros 
disponíveis, e o quarto valor acaba sendo atribuído ao parâmetro bônus.

Quando passamos quatro valores, o Python entende que os três primeiros são as notas e o quarto valor é o bônus. 
No caso de três valores, o bônus é o valor padrão 0.
"""

#Exercício 16 – Unpacking com ** e argumentos nomeados
#
#Considere o seguinte dicionário:
#
#jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}
#
#Crie uma função chamada apresentar_jogador que receba:
#
#nome
#idade
#posicao
#
#A função deve:
#
#Utilizar type hints em todos os parâmetros.
#Indicar através do type hint que a função não retorna nenhum valor.
#Possuir uma docstring.
#Exibir uma mensagem com os dados do jogador.
#
#Chame a função desempacotando o dicionário com **.
#
#Você não deve acessar manualmente:
#
#jogador["nome"]
#jogador["idade"]
#jogador["posicao"]
#
#Depois, responda em um comentário no código:
#
#Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?

def apresentar_jogador(nome: str, idade: int, posicao: str) -> None:
    """Apresenta o jogador"""
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Posição: {posicao}")
    
jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}

apresentar_jogador(**jogador)

"""
As chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função porque o ** faz o mapeamento automático dos valores do
dicionário para os parâmetros correspondentes da função. 
Se as chaves não coincidirem com os nomes dos parâmetros, o Python não saberá como relacioná-las, resultando em um erro.

As chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função porque o ** desempacota o dicionário
como argumentos NOMEADOS, logo, precisamos que as chaves do dicionário sejam correspondentes aos parâmetros.

"""


#Exercício 17 – *args recebendo e * desempacotando
#
#Crie uma função chamada calcular_total_gols que receba uma quantidade variável de números utilizando *args.
#
#A função deve:
#
#Utilizar type hint no *args.
#Possuir uma docstring.
#Somar todos os valores recebidos.
#Retornar o total de gols.
#Considere as listas:
#
#primeiro_tempo = [1, 2, 1]
#segundo_tempo = [2, 1]
#
#
#Chame a função desempacotando as duas listas na mesma chamada:
#
#total = calcular_total_gols(*primeiro_tempo,*segundo_tempo)
#print(total)
#
#
#Depois, escreva comentários no código explicando a diferença entre:
#
#def calcular_total_gols(*gols):...
#e:
#
#calcular_total_gols(*primeiro_tempo)
#
#
#Explique qual * está recebendo vários argumentos e qual está desempacotando uma coleção.


def calcular_total_gols(*gols:int):
    """Calcular o toal de gols"""
    return sum(gols)

primeiro_tempo = [1, 2, 1]
segundo_tempo = [2, 1]

total = calcular_total_gols(*primeiro_tempo, *segundo_tempo)
print(total)

"""
O * que está recebendo vários argumentos é o que está na definição da função calcular_total_gols(*gols:int):
O * que está desempacotando é o que está na chamada da função calcular_total_gols(*primeiro_tempo, *segundo_tempo)
"""

#Exercício 18 – Parâmetros somente posicionais com /
#
#Crie uma função chamada registrar_placar com a seguinte assinatura:
#
#def registrar_placar(time_a: str,time_b: str,/,gols_a: int,gols_b: int) -> str:...
#A função deve:
#
#Possuir uma docstring.
#Utilizar os type hints indicados.
#Retornar uma string contendo o placar da partida.
#Exigir que time_a e time_b sejam passados somente por posição.
#Permitir que gols_a e gols_b sejam passados por posição ou pelo nome.
#
#Faça uma chamada válida utilizando:
#resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
#print(resultado)
#
#Depois, tente:
#
#registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)
#
#Observe o erro e explique em um comentário qual é a função do / na assinatura.


def registrar_placar(time_a: str, time_b: str, / , gols_a: int, gols_b: int) -> str:
    """Registra o placar de uma partida"""
    return f"{time_a} {gols_a} x {gols_b} {time_b}"

resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
print(resultado)

#registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)
"""
#A função do / na assinatura da função é indiciar que tudo que aparece antes dela, deve ser passado como um argumento posicional.
"""


#Exercício 19 – Parâmetros somente nomeados com *
#
#Crie uma função chamada criar_jogador com a seguinte assinatura:
#
#def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:...
#A função deve:
#
#Possuir uma docstring.
#Utilizar type hints.
#Utilizar um valor padrão para titular.
#Retornar uma string com os dados do jogador.
#O parâmetro nome pode ser informado por posição.
#
#Os parâmetros após * devem ser informados pelo nome.
#
#Faça uma chamada válida:
#
#jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
#print(jogador)
#
#Depois, faça outra chamada informando:
#
#titular=True
#
#Por fim, tente executar:
#
#criar_jogador("Marta","Atacante",10)
#
#Observe o erro e explique em um comentário por que posicao e numero não podem ser passados por posição.


def criar_jogador(nome: str, *, posicao: str, numero: int, titular: bool = False) -> str:
    """Cria um jogador"""
    return f"Nome: {nome}, Posicao: {posicao}, Numero: {numero}, Titular: {titular}"

jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
print(jogador)  

jogador2 = criar_jogador("Marta",posicao="Atacante",numero=10, titular=True)
print(jogador2)  

#criar_jogador("Marta","Atacante",10)
"""
Posicao e numero não podem ser passados por posição, pois o * na definição da função indica que
tudo que aparece depois dele deve ser passado como um argumento nomeado.
"""


#Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos
#Crie uma função chamada registrar_jogo com a seguinte assinatura:
#
#def registrar_jogo(
#mandante: str,visitante: str,
#/,
#competicao: str,
#*eventos: str,
#estadio: str,
#encerrado: bool = True,
#**informacoes
#) -> dict:
#
#
#A função deve possuir uma docstring completa explicando:
#
#O objetivo da função.
#O que cada parâmetro representa.
#O que a função retorna.
#
#
#A função também deve seguir estas regras:
#
#mandante e visitante devem ser informados somente por posição.
#competicao pode ser passada por posição ou pelo nome.
#*eventos deve receber uma quantidade variável de eventos da partida.
#estadio deve obrigatoriamente ser informado pelo nome.
#encerrado deve possuir True como valor padrão.
#**informacoes deve receber informações adicionais da partida.
#
#Dentro da função, crie e retorne um dicionário contendo:
#
#Mandante.
#Visitante.
#Competição.
#Eventos.
#Estádio.
#Situação da partida.
#Informações adicionais.
#Teste a função com:
#
#partida = registrar_jogo(
#"Brasil",
#"Argentina",
#"Copa do Mundo",
#"Gol do Brasil",
#"Cartão amarelo",
#"Substituição",
#estadio="Maracanã",
#publico=70000,
#transmissao="TV"
#)
#print(partida)
#
#
#Depois, considere os seguintes dados:
#
#times = ["França", "Espanha"]
#dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}
#
#Faça uma segunda chamada utilizando:
#
#*times para desempacotar os dois primeiros argumentos.
#Uma competição informada normalmente.
#Dois ou mais eventos posicionais.
#**dados para desempacotar as informações nomeadas.
#
#
#Ao final, escreva comentários identificando o papel de cada elemento da assinatura:
#
#/
#*eventos
#estadio
#encerrado=True
#**informacoes
#
#
#Explique também a diferença entre:
#
#*eventos
#na definição da função e:
#
#*times
#na chamada, assim como a diferença entre:
#
#**informacoes
#na definição e:
#
#**dados
#na chamada.

def registrar_jogo(
    mandante: str, 
    visitante: str, 
    /, # Tudo que aparece antes da / deve ser passado como um argumento posicional
    competicao: str, # Pode ser passado como um argumento posicional ou pelo nome
    *eventos: str, # Deve receber uma quantidade variável de eventos da partida
    estadio: str, # Deve ser informado obrigatoriamente pelo nome
    encerrado: bool = True, # Deve possuir True como valor padrão
    **informacoes # Deve receber informações adicionais da partida
) -> dict:
    """Registra um jogo"""

    jogo = {
        "mandante": mandante,
        "visitante": visitante,
        "competicao": competicao,
        "eventos": eventos,
        "estadio": estadio,
        "encerrado": encerrado,
        **informacoes
    }
    return jogo

partida = registrar_jogo(
"Brasil",
"Argentina",
"Copa do Mundo",
"Gol do Brasil",
"Cartão amarelo",
"Substituição",
estadio="Maracanã",
publico=70000,
transmissao="TV"
)
print(partida)    

    
times = ["França", "Espanha"]
dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}    


#*times para desempacotar os dois primeiros argumentos.
#Uma competição informada normalmente.
#Dois ou mais eventos posicionais.
#**dados para desempacotar as informações nomeadas.
partida2 = registrar_jogo(*times, "Eurocopa", "Gol da França", "Pênalti perdido", **dados)
print(partida2)

"""
Explique também a diferença entre *eventos na definição da função e *times na chamada:
*eventos na definição da função, deve receber uma quantidade variável de eventos da partida
*times na chamada, desempacota os dois primeiros argumentos

Assim como a diferença entre **informacoes na definição e **dados na chamada.
**informacoes na definição da função, deve receber informações nomeadas adicionais da partida
**dados na chamada, desempacota as informações nomeadas
"""