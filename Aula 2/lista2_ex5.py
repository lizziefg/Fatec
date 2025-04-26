'''
Exercício 5: Multiplicação de um número por uma string
Peça ao usuário que digite um número inteiro e armazene-o na variável numero.
Depois, peça que digite um caractere ou palavra curta e armazene-a na variável texto.
Multiplique a string pelo número digitado e exiba o resultado
'''

numero = input("Digite um número inteiro: ")
texto = input("Digite um caractere ou palavra curta: ")
#Para que a multiplicação funcione, o valor de string obtido no input da variável numero deve ser transformada em número inteiro
numero = int(numero)
resultado = numero * texto
print(resultado)
