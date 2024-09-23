# 7.  Atualização de Dicionários:  
# Dada uma lista de nomes de alunos e suas respectivas notas em uma prova, crie um 
# dicionário e permita que o usuário consulte e atualize a nota de um aluno específico. 


nomes = ['Luccas, 8', 'Gabriel, 7.8','Adrian, 8.7', 'João, 9.5']
dicionario = {}

for aluno in nomes:
    nome, nota = aluno.split(', ')
    dicionario[nome] = float(nota)

print('Dicionário criado com sucesso!')
print('Dicionário:', dicionario)


# Consultar nota
print('\nConsultar nota de um aluno:')
nome_aluno = input('Digite o nome do aluno: ')
nota_aluno = dicionario.get(nome_aluno, 'Nota não encontrada')
print(f'A nota do aluno {nome_aluno} é {nota_aluno}')


# Atualizar nota
print('\nAtualizar nota de um aluno:')
nome_aluno = input('Digite o nome do aluno: ')
nova_nota = float(input('Digite a nova nota do aluno: '))
dicionario[nome_aluno] = nova_nota

print(f'A nota do aluno {nome_aluno} foi atualizada para {nova_nota}')

print('Dicionário:', dicionario)