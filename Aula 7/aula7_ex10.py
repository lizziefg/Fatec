'''Exercício 10 - Mini-Max Sum
Dados cinco inteiros positivos, encontre os valores mínimo e máximo que podem ser calculados
somando exatamente quatro dos cinco inteiros. Em seguida, imprima os respectivos valores mínimo
e máximo como uma única linha de dois inteiros longos separados por espaços.
Ou seja,
Dado um lista de cinco inteiros positivos, encontre:
• O menor valor possível da soma de quatro dos cinco inteiros.
• O maior valor possível da soma de quatro dos cinco inteiros.
Depois, imprima os dois valores na mesma linha, separados por um espaço.'''

numeros = [2, 3, 5, 7, 8]

menor  = sum(numeros) - max(numeros)
maior = sum(numeros) - min(numeros)

print(menor, maior)