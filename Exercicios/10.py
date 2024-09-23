# 10.  Dicionário Aninhado:  
# Crie um dicionário para armazenar informações sobre estudantes, onde cada chave é o 
# nome de um estudante e o valor é outro dicionário contendo suas notas nas disciplinas 
# "Matemática", "Português" e "Ciências". Permita que o usuário acesse e altere as notas dos 
# alunos. 


dict_estudantes = {
    "Luccas": {"Matemática": 8, "Português": 7, "Ciências": 8.6},
    "Rachel": {"Matemática": 7.3, "Português": 8.7, "Ciências": 8},
    "Pedro": {"Matemática": 9.8, "Português": 7, "Ciências": 6.5},
    }

def ver_alunos():
    for aluno, notas in dict_estudantes.items():
        print(f"Aluno: {aluno}")

def acessar_aluno(nome):
    return dict_estudantes.get(nome, "Aluno não encontrado")


def alterar_aluno(nome, disciplina, nota):
    if nome in dict_estudantes:
        dict_estudantes[nome][disciplina] = nota
    else:
        print("Aluno não encontrado")


def main():
    while True:
        print("1 - Ver Alunos")
        print("2 - Acessar aluno")
        print("3 - Alterar nota de aluno")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_alunos()

        elif opcao == "2":
            nome = input("Digite o nome do aluno: ")
            print(acessar_aluno(nome))

        elif opcao == "3":
            nome = input("Digite o nome do aluno: ")
            disciplina = input("Digite a disciplina: ")
            nota = float(input("Digite a nota: "))
            alterar_aluno(nome, disciplina, nota)

        elif opcao == "4":
            break

main()