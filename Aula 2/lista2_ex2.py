'''
Exercício 2: Soma de dois números
Crie duas variáveis numéricas, num1 e num 2, e atribua valores a elas.
Calcule a soma dessas variáveis e armazene o resultado em uma nova variável soma.
Por fim, exiba a seguinte mensagem:
"A soma de [num1] e [num2] é igual a [soma]."
'''

num1 = 3
num2 = 7
soma = num1 + num2

#Para poder concatenar a expressão é necessário que os valores sejam transformados em string

num1 = str(num1)
num2 = str(num2)
soma = str(soma)

print ("A soma de " + num1 + " e " + num2 + " é igual a " + soma + ".")
