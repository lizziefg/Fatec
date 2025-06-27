'''Exercício 11 - Top 3 Sum
Dada uma lista de números inteiros positivos, calcule:
A soma dos três maiores números da lista.
A soma dos três menores números da lista.
Imprima os dois valores na mesma linha, separados por espaço.'''

numeros = [10, 3, 5, 7, 2, 8, 12]

numeros.sort()
soma_menores = numeros[0] + numeros[1] + numeros[2]

numeros.sort(reverse=True)
soma_maiores = numeros[0] + numeros[1] + numeros[2]

print(f'{soma_maiores} {soma_menores}')