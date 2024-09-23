# 5.  Remoção de Duplicatas:  
# Escreva um programa que receba uma lista de números do usuário e remova todos os 
# números duplicados, exibindo a lista resultante sem repetições.


lista = [1, 3, 3, 4, 5, 6, 7, 4 ,7, 8, 9, 10, 13, 13, 666]

lista = list(set(lista))

print("Lista sem duplicatas: ", lista)