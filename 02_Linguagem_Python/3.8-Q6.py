"""
Desafio Final — Sistema da Copa do Mundo

Desenvolva um programa para cadastrar partidas da Copa do Mundo.
O programa deverá permanecer em execução até que o usuário decida encerrá-lo.

Para cada partida, solicite:

Seleção mandante
Seleção visitante
Gols da seleção mandante
Gols da seleção visitante

Cada partida deverá ser armazenada em um dicionário, e todos os dicionários deverão ser armazenados em uma lista.

Ao finalizar o cadastro, exiba:

A quantidade de partidas cadastradas.
Todas as partidas registradas.
Quantas partidas terminaram empatadas.
A partida com o maior número total de gols.
A média de gols por partida.

Requisitos:

Utilize listas e dicionários.
Utilize while para controlar o cadastro.
Utilize for para percorrer as partidas.
Utilize if, elif e else para identificar o resultado de cada jogo.
Utilize try/except para validar os gols informados.
Utilize len() para calcular a quantidade de partidas cadastradas.
"""

partidas = []

print("Cadastro de Partidas da Copa do Mundo.\n")
while True:
    print("1 - Adicionar partida")
    print("2 - Encerrar cadastro")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        selecao_mandante = input("Digite o nome da seleção mandante: ")
        selecao_visitante = input("Digite o nome da seleção visitante: ")
        while True:
            try:
                gols_mandante = int(input(f"Quantos gols a seleção mandante marcou? "))
                if gols_mandante < 0:
                    print("A quantidade de gols não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
        
        while True:
            try:
                gols_visitante = int(input(f"Quantos gols a seleção visitante marcou? "))
                if gols_visitante < 0:
                    print("A quantidade de gols não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")                
        
        partida = {"selecao_mandante": selecao_mandante, "selecao_visitante": selecao_visitante, "gols_mandante": gols_mandante, "gols_visitante": gols_visitante}
        partidas.append(partida)
    elif opcao == "2":
        print("Encerrando cadastro")
        break
    else:
        print("Opção inválida! Digite 1 ou 2.")

if len(partidas) > 0:
    print("\n--- Análise das Partidas ---")
    print(f"Quantidade de partidas cadastradas: {len(partidas)}")
    
    print("\nPartidas registradas:")
    for partida in partidas:
        print(f"{partida['selecao_mandante']} {partida['gols_mandante']} x {partida['gols_visitante']} {partida['selecao_visitante']}")
    
    empates = 0
    for partida in partidas:
        if partida['gols_mandante'] == partida['gols_visitante']:
            empates += 1
    print(f"\nPartidas empatadas: {empates}")
    
    maior_total_gols = -1
    partida_maior_gols = None
    for partida in partidas:
        total_gols = partida['gols_mandante'] + partida['gols_visitante']
        if total_gols > maior_total_gols:
            maior_total_gols = total_gols
            partida_maior_gols = partida
    print(f"\nPartida com o maior número de gols: {partida_maior_gols['selecao_mandante']} {partida_maior_gols['gols_mandante']} x {partida_maior_gols['gols_visitante']} {partida_maior_gols['selecao_visitante']} ({maior_total_gols} gols no total)")
    
    total_gols_geral = 0
    for partida in partidas:
        total_gols_geral += partida['gols_mandante'] + partida['gols_visitante']
    
    media_gols = total_gols_geral / len(partidas)
    print(f"\nMédia de gols por partida: {media_gols:.2f}")

else:
    print("Nenhuma partida foi cadastrada.")