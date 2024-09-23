# 14.  Função que Modifica Dicionários:  
# Escreva uma função que receba um dicionário representando um estoque de produtos 
# (chave: nome do produto, valor: quantidade em estoque) e um produto vendido (nome do 
# produto e quantidade vendida). A função deve atualizar o estoque conforme a venda e 
# informar se a quantidade vendida excede o estoque disponível. 


qtd_produtos = {
    "Café": 136,
    "Pão": 57,
    "Leite": 157,
    "Frango": 115,
    "Ovos": 93
}

produtos_vendidos = {
    "Café": 22,
    "Pão": 5,
    "Leite": 11,
    "Frango": 6,
    "Ovos": 4
}

def atualiza_estoque(qtd_produtos, produtos_vendidos):

    for produto, qtd_vendida in produtos_vendidos.items():
        if produto in qtd_produtos.keys():

            if qtd_vendida > qtd_produtos[produto]:
                print(f"Quantidade de {produto} vendida excede o estoque disponível.")
                
            else:
                qtd_produtos[produto] -= qtd_vendida
                print(f"Estoque de {produto} atualizado para {qtd_produtos[produto]}")

atualiza_estoque(qtd_produtos, produtos_vendidos)       

print(f"Estoque Final: {qtd_produtos}")