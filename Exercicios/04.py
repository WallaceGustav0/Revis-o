# 4.  Listas Aninhadas:  
# Crie uma lista de listas onde cada sublista deve conter três elementos: o nome de uma 
# pessoa, sua idade e sua cidade. Imprima todas as informações no formato: "Nome: [Nome], 
# Idade: [Idade], Cidade: [Cidade]". 


lista = ['Gabriel, 19, Jaconé', 'Rachel, 24, Araruama', 'Adrian, 19, Barra Nova']
for pessoa in lista:
    nome, idade, cidade = pessoa.split(', ')
    
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")