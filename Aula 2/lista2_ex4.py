'''
Exercício 4: Calculando idade no futuro
Crie uma variável chamada idade_atual e atribua um valor numérico a ela.
Em seguida, calcule quantos anos a pessoa terá em 10 anos e armazene esse valor na variável idade_futura.
Exiba a seguinte mensagem usando formatação de string:
"Hoje você tem [idade_atual] anos. Daqui a 10 anos, terá [idade_futura] anos."
'''
idade_atual = 27
idade_futura = idade_atual + 10

idade_atual = str(idade_atual)
idade_futura = str(idade_futura)

print("Hoje você tem " + idade_atual + " anos. Daqui a 10 anos, terá " + idade_futura + " anos.")
