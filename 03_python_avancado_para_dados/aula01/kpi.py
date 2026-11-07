# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final
valor_bonus = 1000 + (salario * bonus)

# 5) Imprima cálculo do KPI para o usuário
print("Cálculo do KPI:")
print("Salário: R$", salario)
print("Bônus: ", bonus, "%")
print("Valor do bônus: R$", valor_bonus)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print("Olá, ", nome, "!")
print("Seu salário é de R$", salario)
print("Seu bônus é de R$", valor_bonus)
print(f"O usuario {nome} possui o bonus de {valor_bonus}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
