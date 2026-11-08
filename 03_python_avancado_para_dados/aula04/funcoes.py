#Um exemplo clássico dessa abstração é a ordenação de uma lista. Vamos primeiro desenvolver uma função 
# simples em Python que ordena uma lista usando o algoritmo de ordenação por seleção, um método simples 
# mas eficaz para listas pequenas e médias. Em seguida, mostraremos como essa tarefa pode ser realizada 
# de forma mais direta usando o método sort() built-in do Python, que é uma abstração fornecida pela 
# linguagem para realizar a mesma tarefa.

#Função de Ordenação Personalizada
# Implementação do algoritmo de ordenação por seleção

lista = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista)



lista = [64, 34, 25, 12, 22, 11, 90]

def ordernar_lista(lista: list) -> list:
    lista_ordenada = lista.copy()

    for i in range(len(lista_ordenada)):
        for j in range(i+1, len(lista_ordenada)):
            if lista_ordenada[i] > lista_ordenada[j]:
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]

    return lista_ordenada

print(ordernar_lista(lista)) 


#Usando o Método Built-in sort()
#O Python fornece uma abstração poderosa através do método sort(), que pode ordenar listas in-place de 
# maneira eficiente e com uma sintaxe simples.

# Lista de exemplo
lista_exemplo = [64, 34, 25, 12, 22, 11, 90]

# Ordenando a lista com sort()
lista_exemplo.sort()

print("Lista ordenada com método built-in:", lista_exemplo)

#Exercícios de Funções
#16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def somar_lista(lista: list) -> int:
    soma = 0
    for i in lista:
        soma += i
    return soma

print(somar_lista(lista_exemplo))

#17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def primo(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(primo(10))
print(primo(11))

#18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverter_string(s: str) -> str:
    return s[::-1]

print(reverter_string("hello"))

#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def combinacoes(lista: list, numero: int) -> list:
    combinacoes = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == numero:
                combinacoes.append((lista[i], lista[j]))
    return combinacoes

lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
print(combinacoes(lista_exemplo, 10))
print(combinacoes(lista_exemplo, 37))

#20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def ordenar_chaves_dicionario(dicionario: dict) -> list:
    return sorted(dicionario.keys())

dicionario_exemplo = {"b": 2, "a": 1, "c": 3}
print(ordenar_chaves_dicionario(dicionario_exemplo))
