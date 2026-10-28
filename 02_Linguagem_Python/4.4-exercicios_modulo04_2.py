#Exercício 1 – Argumentos posicionais
#
#Crie uma função chamada apresentar_jogador que receba:
#
#nome
#posicao
#A função deve exibir uma mensagem semelhante a:
#
#Jogador: Marta | Posição: Atacante
#Faça a chamada da função passando os dois argumentos por posição.
#
#
#
#Exemplo:
#
#apresentar_jogador("Marta", "Atacante")

def apresentar_jogador(nome:str, posicao:str)->None:
    print(f"Nome: {nome} | Posição: {posicao}")
    

apresentar_jogador("Marta", "Atacante") 

#Exercício 2 – A ordem dos argumentos
#
#Crie uma função chamada mostrar_partida que receba:
#
#mandante
#visitante
#A função deve exibir os dois times no formato:
#
#Brasil x Argentina
#
#
#Faça as seguintes chamadas:
#
#mostrar_partida("Brasil", "Argentina")
#mostrar_partida("Argentina", "Brasil")
#
#
#Observe como a ordem dos argumentos posicionais altera o resultado.

def mostrar_partida(mandante:str, visitante:str)->None:
    print(f"{mandante} x {visitante}")

mostrar_partida("Brasil", "Argentina")
mostrar_partida("Argentina", "Brasil") 

#Exercício 3 – Argumentos nomeados
#
#Crie uma função chamada cadastrar_jogador que receba:
#
#nome
#idade
#posicao
#
#
#Faça a chamada utilizando argumentos nomeados e passe os valores em uma ordem diferente da definida na função.
#
#
#
#Exemplo:
#
#cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)

def cadastrar_jogador(nome:str, idade:int, posicao:str)->None:
    print(f"Nome: {nome} | Idade: {idade} | Posição: {posicao}")
    
cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)


#Exercício 4 – Posicionais e nomeados juntos
#
#Crie uma função chamada registrar_gol que receba:
#
#jogador
#time
#minuto
#
#
#Na chamada da função:
#
#Passe jogador por posição.
#Passe time por posição.
#Passe minuto pelo nome.
#
#
#A função deve exibir uma mensagem semelhante a:
#
#Vini Jr marcou para o Brasil aos 34 minutos.

def registrar_gol(jogador:str, time:str, minuto:int)->None:
    print(f"{jogador} marcou para o {time} aos {minuto} minutos.")

registrar_gol("Vini Jr", "Brasil", minuto=34)

#Exercício 5 – Parâmetro com valor padrão
#
#Crie uma função chamada criar_partida que receba:
#
#time_a
#time_b
#estadio
#
#
#O parâmetro estadio deve possuir o seguinte valor padrão:
#
#"Estádio Nacional"
#
#
#Depois, faça duas chamadas:
#
#Uma sem informar o estádio.
#Outra informando um estádio diferente.


def criar_partida(time_a:str, time_b:str, estadio:str="Estádio Nacional")->None:
    print(f"Partida entre {time_a} e {time_b} no {estadio}.")

criar_partida("Brasil", "Argentina")
criar_partida("Brasil", "Argentina", "Maracanã")

#Exercício 6 – Mais de um valor padrão
#
#Crie uma função chamada registrar_jogador com os seguintes parâmetros:
#
#nome
#posicao="Não informada"
#titular=False
#
#A função deve mostrar os dados do jogador.
#
#
#
#Teste as seguintes chamadas:
#
#registrar_jogador("Marta")
#registrar_jogador("Marta", "Atacante")
#registrar_jogador("Marta", "Atacante", True)

def registrar_jogador(nome:str, posicao:str="Não informada", titular:bool=False)->None:
    print(f"Nome: {nome} | Posição: {posicao} | Titular: {titular}")

registrar_jogador("Marta")
registrar_jogador("Marta", "Atacante")
registrar_jogador("Marta", "Atacante", True)


#Exercício 7 – Alterando apenas um valor padrão
#
#Crie uma função chamada configurar_camisa que receba:
#
#nome
#numero
#tamanho="M"
#cor="amarela"
#
#Faça uma chamada informando uma cor diferente, mas mantendo o tamanho padrão.
#
#Exemplo:
#
#configurar_camisa("Marta", 10, cor="azul")
#
#Observe como o argumento nomeado permite alterar cor sem precisar passar um novo valor para tamanho.

def configurar_camisa(nome:str, numero:int, tamanho:str="M", cor:str="amarela")->None:
    print(f"Nome: {nome} | Número: {numero} | Tamanho: {tamanho} | Cor: {cor}")

configurar_camisa("Marta", 10, cor="azul")


#Exercício 8 – Recebendo vários argumentos com *args
#
#Crie uma função chamada listar_jogadores que receba uma quantidade variável de nomes utilizando *args.
#
#def listar_jogadores(*jogadores):
#
#A função deve percorrer os jogadores recebidos e exibir cada nome.
#
#Teste a função com diferentes quantidades de argumentos:
#
#listar_jogadores("Marta")
#listar_jogadores("Marta","Vini Jr","Alisson")

def listar_jogadores(*jogadores):
    for jogador in jogadores:
        print(jogador)


listar_jogadores("Marta")
listar_jogadores("Marta","Vini Jr","Alisson")


#Exercício 9 – Trabalhando com os valores de *args
#
#Crie uma função chamada somar_gols que receba uma quantidade indefinida de números utilizando *args.
#
#A função deve retornar a soma de todos os valores recebidos.
#
#Exemplo:
#
#total = somar_gols(2, 1, 3, 2)
#print(total)
#
#Resultado esperado: 8


def  somar_gols(*gols:int)->int:
    return sum(gols)

total=somar_gols(2,1,3,2)
print(total)

total=somar_gols(12,4,1,7,0,12,2,10)
print(total)

#Exercício 10 – Parâmetro normal e *args
#
#Crie uma função chamada:
#convocar_selecao(pais, *jogadores)
#
#O primeiro argumento deve representar o país da seleção.
#
#Todos os argumentos posicionais seguintes devem representar os jogadores convocados.
#
#Exemplo de chamada:
#
#convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")
#
#A função deve mostrar primeiro o país e depois cada jogador convocado.



def convocar_selecao(pais:str, *jogadores)->None:
    print(f"Pais: {pais}")
    print("Jogadores:")
    for jogador in jogadores:
        print(f"- {jogador}")

convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")


#Exercício 11 – Recebendo argumentos nomeados com **kwargs
#
#Crie uma função chamada mostrar_jogador que receba uma quantidade variável de argumentos nomeados utilizando **kwargs.
#
#def mostrar_jogador(**dados):
#
#Faça uma chamada semelhante a:
#
#mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")
#
#Dentro da função, percorra os dados recebidos e mostre cada chave junto com seu respectivo valor.

def mostrar_jogador(**dados) -> None:
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_jogador(nome="Marta", idade=40, posicao="Atacante") 


#Exercício 12 – Parâmetro normal e **kwargs
#
#Crie uma função chamada:
#cadastrar_time(nome, **informacoes)

#O nome do time deve ser obrigatório.
#As demais informações podem variar de uma chamada para outra.
#
#Exemplo:
#
#cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)
#
#A função deve mostrar o nome do time e depois todas as informações adicionais recebidas.


def cadastrar_time(nome:str, **informacoes)->None:
    print(f"Time: {nome}")
    print("Informações:")
    for chave, valor in informacoes.items():
        print(f"- {chave}: {valor}")

cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)


#Exercício 13 – *args e **kwargs juntos
#
#Crie uma função chamada:
#
#registrar_partida(time_a, time_b, *eventos, **informacoes):
#Os dois primeiros argumentos devem representar os times da partida.
#
#Os argumentos posicionais extras devem representar eventos ocorridos durante o jogo.
#
#Os argumentos nomeados extras devem representar outras informações sobre a partida.
#
#Exemplo:
#
#registrar_partida(
#"Brasil",
#"Argentina",
#"Gol do Brasil",
#"Cartão amarelo",
#"Gol da Argentina",
#estadio="Maracanã",
#publico=70000
#):
#
#
#A função deve mostrar:
#
#Os dois times.
#Todos os eventos recebidos.
#Todas as informações adicionais.


def registrar_partida(time_a:str, time_b:str, *eventos, **informacoes):
    print(f"Partida: {time_a} x {time_b}")
    print("Eventos:")
    for evento in eventos:
        print(f"- {evento}")
    print("Informações:")
    for chave, valor in informacoes.items():
        print(f"- {chave}: {valor}")

registrar_partida(
"Brasil",
"Argentina",
"Gol do Brasil",
"Cartão amarelo",
"Gol da Argentina",
estadio="Maracanã",
publico=70000
)