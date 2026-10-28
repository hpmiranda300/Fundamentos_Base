#Exercício 1 – Criando suas primeiras variáveis
#
#Crie um programa para armazenar algumas informações sobre uma seleção:
#
#
#nome da seleção;
#quantidade de títulos;
#posição no ranking;
#se está classificada para a Copa.
#
#Ao final, imprima todos os valores na tela.

nome_selecao = "Brasil"
quantidade_titulos = 6
posicao_ranking = 6
classificada_copa = True

print(f"Nome da Seleção: {nome_selecao}")
print(f"Quantidade de Títulos: {quantidade_titulos}")   
print(f"Posição no Ranking: {posicao_ranking}")
print(f"Está classificada para a Copa? {classificada_copa}")

# Exercício 2 – Calculando o placar
#
# Uma seleção marcou 3 gols no primeiro tempo e 2 gols no segundo tempo.
#
# Crie variáveis para armazenar essas duas informações e calcule:
# o total de gols da partida;
# quantos gols foram marcados a mais no primeiro tempo em relação ao segundo.
#
# Ao final, imprima os resultados na tela.

gols_primeiro_tempo = 3
gols_segundo_tempo = 2

total_gols = gols_primeiro_tempo + gols_segundo_tempo
gols_diferenca = gols_primeiro_tempo - gols_segundo_tempo

print(f"Total de gols da partida: {total_gols}")
print(f"Gols marcados a mais no primeiro tempo em relação ao segundo: {gols_diferenca}")


#Exercício 3 – Trabalhando com operadores

#Considere:
#pontos = 7
#vitorias = 2
#saldo_gols = 4

#Crie expressões que respondam às seguintes perguntas:
#A seleção possui mais de 5 pontos?
#A seleção possui exatamente 3 vitórias?
#O saldo de gols é maior ou igual a 0?
#A seleção possui mais de 5 pontos e saldo de gols positivo?
#A seleção possui 3 vitórias ou mais de 6 pontos?

#Mostre o resultado de cada expressão.

pontos = 7
vitorias = 2
saldo_gols = 4

# A seleção possui mais de 5 pontos?
print(pontos > 5) 
# A seleção possui exatamente 3 vitórias?
print(vitorias == 3)
#O saldo de gols é maior ou igual a 0?
print(saldo_gols >= 0) 
#A seleção possui mais de 5 pontos e saldo de gols positivo?
print(pontos > 5 and saldo_gols >0 ) 
#A seleção possui 3 vitórias ou mais de 6 pontos?
print(vitorias == 3 or pontos > 6)

#Exercício 4 – Seleção classificada ou eliminada?
#
#Crie uma variável chamada pontos e atribua a ela uma quantidade de pontos.
#
#Depois, utilizando if e else, faça o programa mostrar: "Seleção classificada!"
#caso tenha 6 pontos ou mais.

#Caso contrário, mostre: "Seleção eliminada."
#
#Teste o programa alterando manualmente o valor da variável para verificar os dois caminhos.

pontos = 6

if pontos >= 6:
    print("Seleção classificada!")
else:
    print("Seleção eliminada.")

pontos = 5

if pontos >= 6:
    print("Seleção classificada!")
else:
    print("Seleção eliminada.")



#Exercício 5 – Avaliando o desempenho da seleção
#
#Crie uma variável chamada pontos.
#
#Utilizando if, elif e else, classifique o desempenho da seleção da seguinte forma:
#
#7 pontos ou mais → Excelente campanha
#de 4 a 6 pontos → Campanha regular
#menos de 4 pontos → Campanha ruim
#
#Teste o programa utilizando diferentes valores para pontos.    

pontos = 3

if pontos >= 7:
    print("Excelente campanha")
elif pontos >= 4:
    print("Campanha regular")
else:
    print("Campanha ruim")


pontos = 5

if pontos >= 7:
    print("Excelente campanha")
elif pontos >= 4:
    print("Campanha regular")
else:
    print("Campanha ruim")

pontos = 7

if pontos >= 7:
    print("Excelente campanha")
elif pontos >= 4:
    print("Campanha regular")
else:
    print("Campanha ruim")


#Exercício 6 – Posição do jogador
#
#Utilizando o input(), peça ao usuário para informar a posição de um jogador. As opções esperadas são:
#goleiro
#defesa
#meio
#ataque
#Armazene a resposta em uma variável chamada posicao.

#Depois, utilize match case para verificar a posição informada e mostrar uma mensagem correspondente à função daquele jogador em campo.
#Por exemplo: Digite a posição do jogador: ataque
#Saída esperada: Responsável principalmente pela criação e finalização das jogadas ofensivas.
#Crie também um caso para quando o usuário digitar uma posição diferente das opções esperadas. Nesse caso, mostre: Posição inválida.    

#posicao = input("Digite a posição do jogador: ")
posicao = "teste"

match posicao:
    case "goleiro":
        print("Responsável principalmente pela defesa do gol.")
    case "defesa":
        print("Responsável principalmente pela defesa do gol.")
    case "meio":
        print("Responsável principalmente pela criação e finalização das jogadas ofensivas.")
    case "ataque":
        print("Responsável principalmente pela criação e finalização das jogadas ofensivas.")
    case _:
        print("Posição inválida.")


#Exercício 7 – Simulando as cinco cobranças de pênalti
#
#Uma disputa de pênaltis começa com cinco cobranças para uma equipe.
#
#Utilize for e range() para mostrar na tela:
#Cobrança 1
#Cobrança 2
#Cobrança 3
#Cobrança 4
#Cobrança 5
#Depois das cinco repetições, mostre: "Fim das cobranças iniciais."

for cobranca in range(1, 6):
    print(f"Cobrança {cobranca}")
print("Fim das cobranças iniciais.")


#Exercício 8 – Contando gols
#
#Crie uma variável: gols = 0
#
#Depois, utilize um for para simular 5 oportunidades de gol.
#A cada repetição, acrescente 1 à variável gols e mostre a quantidade atual.
#O resultado deve seguir esta ideia:
#Gol! Total: 1
#Gol! Total: 2
#Gol! Total: 3
#...
#Ao final, mostre a quantidade total de gols.

gols = 0

for i in range(1, 6):
    gols += 1
    print(f"Gol! Total: {gols}")
print(f"Total de gols: {gols}")


#Exercício 9 – Continue até o usuário decidir parar
#
#Crie um programa que permaneça em execução enquanto o usuário responder: "sim"
#A cada repetição, mostre: "Treino iniciado!"
#
#Depois, pergunte novamente: "Deseja realizar outro treino?"
#Quando a resposta for diferente de sim, o while deve terminar e o programa deve mostrar: "Treino encerrado."
#Não é necessário trabalhar com números neste exercício. Utilize a resposta do input() como texto.

resposta = "sim"

while resposta == "sim":
    print("Treino iniciado!")
    resposta = input("Deseja realizar outro treino? ")

print("Treino encerrado.")


#Exercício 10 – Simulando uma sequência de cobranças
#Crie um pequeno programa para representar uma disputa de cinco pênaltis.
#Para cada cobrança, o programa deve perguntar ao usuário: "Resultado da cobrança: gol ou perdeu?"
#Utilize um for para garantir que sejam realizadas exatamente 5 cobranças.
#A cada resposta:
#se for gol, aumente o contador de gols em 1;
#se for perdeu, não aumente o contador;
#se for qualquer outro valor, mostre que a opção informada não foi reconhecida.

#Ao final das cinco cobranças:
#se a seleção tiver marcado 4 ou 5 gols, mostre: "Ótimo desempenho nos pênaltis!";
#se tiver marcado 2 ou 3, mostre: "Desempenho regular nos pênaltis.";
#se tiver marcado 0 ou 1, mostre: "Desempenho ruim nos pênaltis."
#Por fim, mostre também a quantidade total de gols marcados.

#Para resolver esta questão, combine conteúdos estudados ao longo do módulo, como:
#variáveis;
#valores booleanos e comparações;
#input();
#if, elif e else;
#for;
#contador com +=


gols = 0

for cobranca in range(1, 6):
    resultado = input(f"Resultado da cobrança {cobranca}: gol ou perdeu? ")
    if resultado == "gol":
        gols += 1
    elif resultado != "perdeu":
        print("Opção inválida.")

if gols >= 4:
    print("Ótimo desempenho nos pênaltis!")
elif gols >= 2:
    print("Desempenho regular nos pênaltis.")
else:
    print("Desempenho ruim nos pênaltis.")

print(f"Total de gols marcados: {gols}")