# 2.  Operações com Listas:  
# Escreva um programa que receba 5 nomes de frutas do usuário e os armazene em uma lista. 
# Depois, peça ao usuário que informe uma fruta e verifique se ela está na lista. 


frutas = []
for i in range(5):
    fruta = input("Digite o nome de uma fruta: ")
    frutas.append(fruta)
    
fruta = input("Digite o nome de uma fruta para verificar: ")
if fruta in frutas:
    print(f"A fruta {fruta} está disponível.")
else:
    print(f"A fruta {fruta} não está disponível.")