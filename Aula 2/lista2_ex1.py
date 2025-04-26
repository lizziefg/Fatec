'''
Exercício 1: Criando e imprimindo variáveis
Crie três variáveis em Python:
- Uma variável chamada nome para armazenar seu nome.
- Uma variável chamada idade para armazenar sua idade.
- Uma variável chamada altura para armazenar sua altura em metros.
Imprima uma mensagem usando essas variáveis no seguinte formato:
"Meu nome é [nome], tenho [idade] anos e minha altura é [altura] metros."
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')

#O comando input exigirá a entrada de informação pelo usuário, linha a linha.

print("Meu nome é " + nome + ", tenho " + idade + " anos e minha altura é " + altura + " metros.")

#O comando print fará a concatenação do texto com variáveis do tipo string, utilizando o operador +
