"""
Exercício 5 — Ranking de Artilheiros

Crie uma lista de dicionários para armazenar informações de jogadores.

O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.

Para cada jogador, solicite:
Nome
Seleção
Quantidade de gols

Cada jogador deverá ser armazenado como um dicionário dentro da lista.

Ao final:
Exiba todos os jogadores cadastrados.
Informe qual jogador marcou mais gols.
Informe a média de gols dos jogadores cadastrados.

Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.
"""

jogadores = []

numero_jogadores = int(input("Digite quantos jogadores deseja cadastrar: "))

for i in range(1, numero_jogadores + 1):
    nome = input("Digite o nome do jogador: ")
    selecao = input("Digite a seleção do jogador: ")
    gols = int(input("Digite a quantidade de gols do jogador: "))    

    dados_jogador = {
        "nome": nome,
        "selecao": selecao,
        "gols": gols
    }
    
    jogadores.append(dados_jogador)

print("\nJogadores cadastrados:")
for jogador in jogadores:
    print(f"Nome: {jogador['nome']}, Seleção: {jogador['selecao']}, Gols: {jogador['gols']}")   

maior_numero_gols = -1
jogador_com_maior_numero_gols = None
for jogador in jogadores:
    if jogador["gols"] > maior_numero_gols:
        maior_numero_gols = jogador["gols"]
        jogador_com_maior_numero_gols = jogador["nome"]
    
print(f"Jogador com mais gols: {jogador_com_maior_numero_gols}")

soma_gols=0
for jogador in jogadores:
    soma_gols+=jogador["gols"]

media_gols=soma_gols/numero_jogadores
print(f"Média de gols: {media_gols}")