# 11.  Função com Listas:  
# Escreva uma função que receba uma lista de números e retorne a soma de todos os 
# números pares dessa lista. 


def soma_lista():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma

resultado = soma_lista()
print(f"A soma dos números pares é: {resultado}")