'''
Exercício 7: Criando um identificador de usuário
Peça ao usuário que digite seu primeiro nome e ano de nascimento.
Crie um identificador concatenando o nome com o ano e exiba o resultado.
'''
primeiro_nome = input("Digite seu primeiro nome: ")
ano_nascimento = input("Digite seu ano de nascimento: ")
#A resposta dos inputs gera um valor de string, podendo ser concatenado
print("Seu identificador de usuário é: " + primeiro_nome + ano_nascimento)
