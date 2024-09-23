# 9.  Conversão entre Listas e Dicionários:  
# Crie duas listas: uma com nomes de países e outra com suas respectivas capitais. Converta 
# essas duas listas em um dicionário, onde o país é a chave e a capital é o valor.


paises = ['Brasil','Argentina','Chile','Russia']
capitais = ['Brasília','Buenos Aires','Santiago','Moscou']

dicionario = dict(zip(paises, capitais))
print(dicionario)