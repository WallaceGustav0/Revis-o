# 13.  Função com Parâmetros Opcionais:  
# Crie uma função que recebe uma lista e um número opcional. Se o número for fornecido, a 
# função deve retornar a lista multiplicada por esse número. Se não for fornecido, a função deve 
# retornar a lista original. 


lista = [3, 4, 5, 7, 13, 21]

def multiplicar_lista(lista, numero=None):
    if numero is not None:
        return [i * numero for i in lista]
    else:
        return lista
    
numero = 5

print(multiplicar_lista(lista, numero))
