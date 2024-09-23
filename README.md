Exercícios de Listas 

1.  Criação e Manipulação de Listas:  
Crie uma lista com 10 números inteiros aleatórios e escreva um programa para imprimir o 
maior e o menor número dessa lista.

2.  Operações com Listas:  
Escreva um programa que receba 5 nomes de frutas do usuário e os armazene em uma lista. 
Depois, peça ao usuário que informe uma fruta e verifique se ela está na lista.

3.  Manipulação de Listas com Laços:  
Crie uma lista de 10 elementos numéricos e escreva uma função que calcule a média dos 
números presentes na lista.

4.  Listas Aninhadas:  
Crie uma lista de listas onde cada sublista deve conter três elementos: o nome de uma 
pessoa, sua idade e sua cidade. Imprima todas as informações no formato: "Nome: [Nome], 
Idade: [Idade], Cidade: [Cidade]".

5.  Remoção de Duplicatas:  
Escreva um programa que receba uma lista de números do usuário e remova todos os 
números duplicados, exibindo a lista resultante sem repetições.


Exercícios de Dicionários  

6.  Criação e Acesso a Dicionários:  
Crie um dicionário que armazene os dias da semana como chaves e o número de horas 
trabalhadas em cada dia como valores. Solicite ao usuário a entrada dessas horas e depois 
calcule o total de horas trabalhadas na semana.

7.  Atualização de Dicionários:  
Dada uma lista de nomes de alunos e suas respectivas notas em uma prova, crie um 
dicionário e permita que o usuário consulte e atualize a nota de um aluno específico.

8.  Iteração sobre Dicionários:  
Crie um dicionário que armazene a quantidade de produtos em estoque em uma loja. 
Escreva uma função que verifique se um produto está em estoque e quantas unidades estão 
disponíveis.

9.  Conversão entre Listas e Dicionários:  
Crie duas listas: uma com nomes de países e outra com suas respectivas capitais. Converta 
essas duas listas em um dicionário, onde o país é a chave e a capital é o valor.

10.  Dicionário Aninhado:  
Crie um dicionário para armazenar informações sobre estudantes, onde cada chave é o 
nome de um estudante e o valor é outro dicionário contendo suas notas nas disciplinas 
"Matemática", "Português" e "Ciências". Permita que o usuário acesse e altere as notas dos 
alunos.


Exercícios de Funções  

11.  Função com Listas:  
Escreva uma função que receba uma lista de números e retorne a soma de todos os 
números pares dessa lista.

12.  Função que Trabalha com Dicionários:  
Escreva uma função que receba um dicionário contendo nomes de produtos como chaves e 
seus preços como valores. A função deve retornar o nome do produto mais caro.

13.  Função com Parâmetros Opcionais:  
Crie uma função que recebe uma lista e um número opcional. Se o número for fornecido, a 
função deve retornar a lista multiplicada por esse número. Se não for fornecido, a função deve 
retornar a lista original.

14.  Função que Modifica Dicionários:  
Escreva uma função que receba um dicionário representando um estoque de produtos 
(chave: nome do produto, valor: quantidade em estoque) e um produto vendido (nome do 
produto e quantidade vendida). A função deve atualizar o estoque conforme a venda e 
informar se a quantidade vendida excede o estoque disponível.

15.  Combinação de Listas, Dicionários e Funções:  
Escreva uma função que recebe uma lista de dicionários, onde cada dicionário representa 
um estudante com seu nome e uma lista de notas. A função deve calcular a média de cada 
estudante e retornar um novo dicionário com os nomes dos estudantes como chaves e suas 
médias como valores.

16. Funções Recursivas: 
Escreva uma função de busca binária recursiva



Tarefa de Implementação  

Descrição do Sistema 

O sistema de gerenciamento de estoque de livros permite que a biblioteca cadastre, atualize, 
remova, e busque livros, bem como verifique a quantidade de exemplares disponíveis de cada 
livro. Os livros serão armazenados em uma lista, onde cada elemento é um dicionário que 
representa um livro com informações como título, autor, gênero, quantidade em estoque e 
código do livro. O sistema usará diversas funções para manipular a lista de dicionários. 

Atores 
• Bibliotecário: Responsável por gerenciar o estoque de livros. 

Fluxo Principal de Casos de Uso 

1. Cadastrar Livro 
o O bibliotecário pode cadastrar um novo livro no sistema, informando o título, 
autor, gênero, quantidade e código do livro.

o O sistema armazena esses dados em um dicionário e adiciona o dicionário à lista 
de livros.


2. Buscar Livro por Código 
o O bibliotecário pode buscar um livro pelo seu código.

o O sistema percorre a lista de livros para encontrar o dicionário que contém o 
código informado e retorna os detalhes do livro. Se o livro não for encontrado, 
uma mensagem de erro é exibida. 


3. Atualizar Estoque de um Livro 
o O bibliotecário pode atualizar a quantidade de exemplares de um livro 
específico.

o O sistema localiza o livro pelo código e atualiza o valor da chave "quantidade" no 
dicionário correspondente. 


4. Remover Livro do Sistema 
o O bibliotecário pode remover um livro do estoque, informando o código do livro.

o O sistema procura o livro pelo código e remove o dicionário correspondente da 
lista. 


5. Listar Todos os Livros 
o O bibliotecário pode solicitar a listagem de todos os livros cadastrados no 
sistema.

o O sistema percorre a lista de livros e exibe as informações de cada dicionário, 
como título, autor, gênero, quantidade e código. 


Requisitos Funcionais 
1. O sistema deve permitir o cadastro de um livro com título, autor, gênero, quantidade e 
código. 
2. O sistema deve permitir a busca de um livro pelo código e retornar suas informações. 
3. O sistema deve permitir a atualização do estoque de um livro específico. 
4. O sistema deve possibilitar a remoção de um livro através de seu código. 
5. O sistema deve listar todos os livros cadastrados no sistema.


Requisitos Não Funcionais 
1. O sistema deve ser simples e de fácil uso para o bibliotecário. 
2. O sistema deve processar as operações de cadastro, busca, atualização, remoção e 
listagem em menos de 2 segundos. 
3. Mensagens de erro devem ser exibidas caso o livro não seja encontrado ou os dados 
inseridos estejam incorretos. 
