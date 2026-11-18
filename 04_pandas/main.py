import pandas as pd

dados = {
    "Nome": ["João", "Maria", "Pedro"],
    "Idade": [25, 30, 35],
    "Salario": [3000, 4500, 5000]
}

df = pd.DataFrame(dados)

print(df)

print("\nMédia salarial:")
print(df["Salario"].mean())