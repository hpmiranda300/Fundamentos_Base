"""
Exercício 2 — Estatísticas da Partida

Crie um programa que solicite ao usuário as seguintes informações de uma partida:

Seleção mandante
Seleção visitante
Gols da seleção mandante
Gols da seleção visitante

Armazene essas informações em um dicionário.

Depois:

Exiba todas as informações utilizando um for com .items().
Informe qual seleção venceu a partida.
Caso os gols sejam iguais, informe que a partida terminou empatada.

Desafio: utilize try/except para garantir que a quantidade de gols seja um número inteiro válido.
"""

# 1. Coleta das seleções
mandante = input("Seleção mandante: ")
visitante = input("Seleção visitante: ")

# 2. Coleta dos gols da selecao mandante com validação (Desafio)
while True:
    try:
        gols_mandante = int(input(f"Gols de {mandante}: "))
        if gols_mandante < 0:
            print("A quantidade de gols não pode ser negativa.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# 2. Coleta dos gols da selecao visitante com validação (Desafio)
while True:
    try:
        gols_visitante = int(input(f"Gols de {visitante}: "))
        if gols_visitante < 0:
            print("A quantidade de gols não pode ser negativa.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# 3. Armazenando em um dicionário
partida = {
    "Seleção Mandante": mandante,
    "Seleção Visitante": visitante,
    "Gols Mandante": gols_mandante,
    "Gols Visitante": gols_visitante
}

# 4. Exibindo as informações com .items()
print("\n--- Estatísticas da Partida ---")
for chave, valor in partida.items():
    print(f"{chave}: {valor}")

# 5. Determinando o resultado
print("\n--- Resultado Final ---")
if partida["Gols Mandante"] > partida["Gols Visitante"]:
    print(f"Vitória de {partida['Seleção Mandante']}!")
elif partida["Gols Visitante"] > partida["Gols Mandante"]:
    print(f"Vitória de {partida['Seleção Visitante']}!")
else:
    print("A partida terminou empatada.")
