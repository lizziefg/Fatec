'''
Exercício 8: Calculando desconto
Crie uma variável preco_original e atribua um valor numérico a ela.
Crie outra variável chamada desconto (em porcentagem, por exemplo, 10 para 10%).
Calcule o preço final após o desconto e exiba a seguinte mensagem:
"O produto que custava [preco_original] com deconto de [desconto]% agora custa [preco_final]."
'''
preco_original = 42.0
desconto = 15
preco_final = (preco_original * (100 - desconto))/100
print(f"O produto que custava {preco_original} com desconto de {desconto}% agora custa {preco_final}.")
