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
#No input dos valores posso ter tipos de informações diferentes do esperado e com isso o programa pode dar erro.

#Ex: Se o usuário digitar uma letra onde solicito o valor do salario ou do bonus, o programa irá quebrar, pois não conseguirá 
# multiplicar um tipo string por um float.

#Ex: Se o usuario digitar número negativo, como -50, o programa irá calcular normalmente e mostrar um resultado negativo
#o que não é esperado, pois o usuario não recebe bonus negativo. 
