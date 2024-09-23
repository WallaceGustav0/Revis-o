# 3.  Manipulação de Listas com Laços:  
# Crie uma lista de 10 elementos numéricos e escreva uma função que calcule a média dos 
# números presentes na lista. 


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def media(lista):
    return sum(lista) / len(lista)

print(media(lista))