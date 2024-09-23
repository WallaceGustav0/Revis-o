# 8.  Iteração sobre Dicionários:  
# Crie um dicionário que armazene a quantidade de produtos em estoque em uma loja. 
# Escreva uma função que verifique se um produto está em estoque e quantas unidades estão 
# disponíveis.


qtd_produtos = {
    "Café": 136,
    "Pão": 57,
    "Leite": 157,
    "Frango": 115,
    "Ovos": 93
}

def verificar_estoque(produto):
    if produto in qtd_produtos:
        return f"O produto {produto} está em estoque e há {qtd_produtos[produto]} unidades disponíveis."
    else:
        return f"O produto {produto} não está em estoque."

print(verificar_estoque("Café"))