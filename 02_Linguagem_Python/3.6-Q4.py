"""
Exercício 4 — Menu do Álbum

Desenvolva um programa que simule um álbum de figurinhas.

Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:

1 - Adicionar figurinha
2 - Remover figurinha
3 - Buscar figurinha
4 - Mostrar álbum
5 - Encerrar

O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.

Regras:

Ao adicionar, a figurinha deve ser inserida no final da lista.
Ao remover, informe caso a figurinha não exista.
Na busca, informe se a figurinha está ou não no álbum.
Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.

Desafio: utilize if, elif, else e while.
"""

album = []

#menu de opçoes
while True:
    print("\n--- MENU DO ÁLBUM ---")
    print("1 - Adicionar figurinha")
    print("2 - Remover figurinha")
    print("3 - Buscar figurinha")
    print("4 - Mostrar álbum")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        #adicionar figurinha
        album.append(input("Digite o nome da figurinha: "))
    elif opcao == "2":
        #remover figurinha
        album.remove(input("Digite o nome da figurinha: "))
    elif opcao == "3":
        #buscar figurinha
        if input("Digite o nome da figurinha: ") in album:
            print("Figurinha encontrada!")
        else:
            print("Figurinha não encontrada!")
    elif opcao == "4":
        #mostrar álbum
        print("\n--- Figurinhas no Álbum ---")
        if len(album) > 0:
            for item in album:
                print(f"- {item}")
        else:
            print("O álbum ainda está vazio.")
    elif opcao == "5":
        #encerrar
        print("Encerrando...")
        break
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")    
