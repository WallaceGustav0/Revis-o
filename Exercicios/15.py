# 15.  Combinação de Listas, Dicionários e Funções:  
# Escreva uma função que recebe uma lista de dicionários, onde cada dicionário representa 
# um estudante com seu nome e uma lista de notas. A função deve calcular a média de cada 
# estudante e retornar um novo dicionário com os nomes dos estudantes como chaves e suas 
# médias como valores. 


lista = [
    {"nome": "Adrian", "notas": [10, 8, 7.8]},
    {"nome": "Rachel", "notas": [7.3, 9, 8]},
    {"nome": "Pedro", "notas": [8.2, 8, 7.6]},
    {"nome": "Luccas", "notas": [8, 9, 6.5]}
]


def calcular_media(lista):
    media = {}
    for estudante in lista:
        media[estudante["nome"]] = sum(estudante["notas"]) / len(estudante["notas"])
    return media

medias = calcular_media(lista)
for nome, media in medias.items():
    print(f" A média de {nome} é: {media:.1f}")