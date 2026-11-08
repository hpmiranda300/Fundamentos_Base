# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
valor1=int(input("Digite um número inteiro: "))
valor2=int(input("Digite outro número inteiro: "))
print(f"A soma dos valores é : {(valor1) + (valor2)}")   

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
valor=int(input("Digite um numero:"))
resto=valor % 5
print("O resto da divisão de", valor, "por 5 é", resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print(f"O resultado da multiplicação de {valor1} por {valor2} é : {(valor1) * (valor2)}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print(f"A divisão inteira de {valor1} por {valor2} é {valor1 // valor2}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print(f"O quadrado de {valor} é {valor * valor}")
print(f"O quadrado de {valor} é {valor ** 2}")

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
float1=float(input("Digite um numero flutuante: "))
float2=float(input("Digite outro numero flutuante: "))
print(f"O valor da adição de {float1} e {float2} é : {(float1)+(float2)}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print(f"A média de {float1} e {float2} é: {(float1 + float2) / 2}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base=float(input("Digite a base: "))
expoente=float(input("Digite o expoente: "))
print(f"A potencia de {base} elevado a {expoente} é: {base ** expoente}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius=float(input("Digite a temperatura em Celsius: "))
fahrenheit=(celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio=float(input("Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print(f"A área do círculo é: {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string1=str(input("Digite uma string: "))
print(f"A string em maiúsculas é: {string1.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo=input("Digite seu nome completo: ")
print(f"O nome em minúsculas é: {nome_completo.lower()}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no 
# início e no final.
frase=input("Digite uma frase: ")
print(f"A frase sem espaços em branco no início e no final é: {frase.strip()}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, 
# imprima o dia, o mês e o ano separadamente.
data=input("Digite uma data no formato dd/mm/aaaa: ") 
dia, mes, ano = data.split("/") 
print(f"Dia: {dia} Mês: {mes} Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
strong2=input("Digite outra string: ")
print(f"A concatenação das strings é: {string1 + strong2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool1=bool(input("Digite um valor booleano: "))
bool2=bool(input("Digite outro valor booleano: "))
print(f"O resultado da operação AND entre {bool1} e {bool2} é: {bool1 and bool2}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print(f"O resultado da operação OR entre {bool1} e {bool2} é: {bool1 or bool2}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print(f"O valor invertido de {bool1} é: {not bool1}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print(f"Resultado da igualdade: {(valor1 == valor2)}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print(f"Resultado da diferença: {(valor1 != valor2)}")

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")


