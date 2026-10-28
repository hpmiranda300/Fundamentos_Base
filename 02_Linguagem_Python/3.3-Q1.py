"""
Exercício 1 — Cadastro de Figurinhas

Você foi contratado para desenvolver um sistema simples para controlar um álbum de figurinhas da Copa do Mundo.
O programa deve permitir que o usuário cadastre figurinhas até que ele digite a palavra "fim".

Ao final, exiba:
Todas as figurinhas cadastradas.
A quantidade total de figurinhas.
A primeira figurinha cadastrada.
A última figurinha cadastrada.

Desafio: não permita que o usuário cadastre uma figurinha vazia.
"""

figurinhas = []

while True:
    entrada = input("Digite o nome da figurinha (ou 'fim' para encerrar): ").strip()

    # Condição de saída
    if entrada.lower() == "fim":
        break

    # Desafio: impede cadastro de figurinha vazia
    if entrada == "":
        print("A figurinha não pode ser vazia! Tente novamente.")
        continue

    # Adiciona a figurinha à lista
    figurinhas.append(entrada)
    print(f"Figurinha '{entrada}' cadastrada com sucesso!")

# Exibição dos resultados
print("\n--- Resumo do Álbum ---")

if len(figurinhas) > 0:
    print(f"Todas as figurinhas cadastradas: {figurinhas}")
    print(f"Quantidade total de figurinhas: {len(figurinhas)}")
    print(f"Primeira figurinha cadastrada: {figurinhas[0]}")
    print(f"Última figurinha cadastrada: {figurinhas[-1]}")
else:
    print("Nenhuma figurinha foi cadastrada.")

