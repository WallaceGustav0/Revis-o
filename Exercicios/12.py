# 12.  Função que Trabalha com Dicionários:  
# Escreva uma função que receba um dicionário contendo nomes de produtos como chaves e 
# seus preços como valores. A função deve retornar o nome do produto mais caro. 


dict_produtos = {
    "Cachorro Quente": 7.50,
    "X-Salada": 13.00,
    "Refrigerante": 5.99,
    "Pão de Queijo": 3.99,
    }

def produto_caro(dicionario):
    return max(dicionario, key=dicionario.get)

produto_mais_caro = produto_caro(dict_produtos)
preco = dict_produtos[produto_mais_caro]

print(f"O produto mais caro é: {produto_mais_caro}, e custa: R${preco:.2f}")