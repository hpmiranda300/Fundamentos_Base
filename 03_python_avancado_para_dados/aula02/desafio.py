### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

# 4) Calcule o valor do bônus final
# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?









