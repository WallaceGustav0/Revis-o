# Tarefa de Implementação  

# Descrição do Sistema 

# O sistema de gerenciamento de estoque de livros permite que a biblioteca cadastre, atualize, 
# remova, e busque livros, bem como verifique a quantidade de exemplares disponíveis de cada 
# livro. Os livros serão armazenados em uma lista, onde cada elemento é um dicionário que 
# representa um livro com informações como título, autor, gênero, quantidade em estoque e 
# código do livro. O sistema usará diversas funções para manipular a lista de dicionários. 

# Atores 
# • Bibliotecário: Responsável por gerenciar o estoque de livros. 

# Fluxo Principal de Casos de Uso 

# 1. Cadastrar Livro 

# o O bibliotecário pode cadastrar um novo livro no sistema, informando o título, 
# autor, gênero, quantidade e código do livro. 

# o O sistema armazena esses dados em um dicionário e adiciona o dicionário à lista 
# de livros. 


# 2. Buscar Livro por Código 
# o O bibliotecário pode buscar um livro pelo seu código. 

# o O sistema percorre a lista de livros para encontrar o dicionário que contém o 
# código informado e retorna os detalhes do livro. Se o livro não for encontrado, 
# uma mensagem de erro é exibida.
#  
# 3. Atualizar Estoque de um Livro 
# o O bibliotecário pode atualizar a quantidade de exemplares de um livro 
# específico. 

# o O sistema localiza o livro pelo código e atualiza o valor da chave "quantidade" no 
# dicionário correspondente.
# 
#  
# 4. Remover Livro do Sistema 

# o O bibliotecário pode remover um livro do estoque, informando o código do livro.
#  
# o O sistema procura o livro pelo código e remove o dicionário correspondente da 
# lista. 


# 5. Listar Todos os Livros 

# o O bibliotecário pode solicitar a listagem de todos os livros cadastrados no 
# sistema. 

# o O sistema percorre a lista de livros e exibe as informações de cada dicionário, 
# como título, autor, gênero, quantidade e código. 


# Requisitos Funcionais 
# 1. O sistema deve permitir o cadastro de um livro com título, autor, gênero, quantidade e 
# código. 
# 2. O sistema deve permitir a busca de um livro pelo código e retornar suas informações. 
# 3. O sistema deve permitir a atualização do estoque de um livro específico. 
# 4. O sistema deve possibilitar a remoção de um livro através de seu código. 
# 5. O sistema deve listar todos os livros cadastrados no sistema. 


# Requisitos Não Funcionais 
# 1. O sistema deve ser simples e de fácil uso para o bibliotecário. 
# 2. O sistema deve processar as operações de cadastro, busca, atualização, remoção e 
# listagem em menos de 2 segundos. 
# 3. Mensagens de erro devem ser exibidas caso o livro não seja encontrado ou os dados 
# inseridos estejam incorretos.


livros = []

def cadastrar_livros():
    while True:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        genero = input("Digite o gênero do livro: ")
        quantidade = int(input("Digite a quantidade de exemplares do livro: "))
        codigo = input("Digite o código do livro: ")
        
        livro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "quantidade": quantidade,
            "codigo": codigo
            }
        
        livros.append(livro)
        resposta = input("Deseja cadastrar mais um livro? (s/n): ")
        if resposta.lower() != "s":
            break


def buscar_livro(livros):
    codigo = input("Digite o código do livro que deseja buscar: ")
    for livro in livros:
        if livro["codigo"] == codigo:
            print(f"Título: {livro['titulo']}\nAutor: {livro['autor']}\nGênero: {livro['genero']}\nQuantidade: {livro['quantidade']}\nCódigo: {livro['codigo']}")
            return
    print("Livro não encontrado.")


def atualizar_estoque(livros):
    codigo = input("Digite o código do livro que deseja atualizar o estoque: ")
    for livro in livros:
        if livro["codigo"] == codigo:
            quantidade = int(input("Digite a nova quantidade de exemplares do livro: "))
            livro["quantidade"] = quantidade
            print("Estoque atualizado com sucesso!")
            return
    print("Livro não encontrado.")

    
def remover_livro(livros):
    codigo = input("Digite o código do livro que deseja remover: ")
    for livro in livros:
        if livro["codigo"] == codigo:
            livros.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Livro não encontrado.")


def listar_livros(livros):
    for livro in livros:
        print(f"Título: {livro['titulo']}\nAutor: {livro['autor']}\nGênero: {livro['genero']}\nQuantidade{livro['quantidade']}\nCódigo: {livro['codigo']}")
        print("\n")


def menu():
            while True:
                print("\nBiblioteca")
                print("1 - Cadastrar livro")
                print("2 - Buscar livro")
                print("3 - Atualizar estoque")
                print("4 - Remover livro")
                print("5 - Listar Livros")
                print("6 - Sair")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    cadastrar_livros()

                elif escolha == "2":
                    buscar_livro(livros)

                elif escolha == "3":
                    atualizar_estoque(livros)

                elif escolha == "4":
                    remover_livro(livros)

                elif escolha == "5":
                    listar_livros(livros)

                elif escolha == "6":
                    print("Obrigado por usar a biblioteca!")
                    break

                else:
                    print("Opção inválida. Por favor, tente novamente.")

menu()