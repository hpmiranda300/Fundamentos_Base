"""
Exercício 3 — Seleções Classificadas

Durante a fase de grupos, várias seleções foram sendo classificadas.
Peça ao usuário para informar o nome de 8 seleções.
Armazene essas seleções em um set.

Ao final:
Exiba todas as seleções classificadas.
Informe quantas seleções diferentes foram cadastradas.

Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.

Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
"""

selecoes_classificadas = set()
for i in range(1, 9):
    selecao = input(f"Informe o nome de 8 seleções, uma seleção por vez ({i})?")
    selecoes_classificadas.add(selecao)


print(selecoes_classificadas)
print(f"Foram cadastradas {len(selecoes_classificadas)} seleções diferentes")

selecao_escolhida = input("Informe o nome de uma seleção para verificar se ela está classificada: ")
if selecao_escolhida in selecoes_classificadas:
    print(f"{selecao_escolhida} está classificada!")
else:
    print(f"{selecao_escolhida} não está classificada!")


#Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
#Resp: A estrtura de dados set, não aceita elementos repetidos.








