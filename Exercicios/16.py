# 16. Funções Recursivas: 
# Escreva uma função de busca binária recursiva 


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def busca_binaria(lista, valor, inicio, fim):
    if inicio > fim:
        return False
    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        return True
    
    elif lista[meio] < valor:
        return busca_binaria(lista, valor, meio + 1, fim)
    
    else:
        return busca_binaria(lista, valor, inicio, meio - 1)

print(busca_binaria(lista, 7, 0, len(lista) - 1))