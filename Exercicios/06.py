# 6.  Criação e Acesso a Dicionários:  
# Crie um dicionário que armazene os dias da semana como chaves e o número de horas 
# trabalhadas em cada dia como valores. Solicite ao usuário a entrada dessas horas e depois 
# calcule o total de horas trabalhadas na semana. 

semanas = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0,
}

horas_trabalhadas = 0

for dia in semanas:
    horas = int(input(f"Quantas horas você trabalhou {dia}: "))
    semanas[dia] = horas
    horas_trabalhadas += horas
    
    print(f"Total de horas trabalhadas na semana: {horas_trabalhadas}")