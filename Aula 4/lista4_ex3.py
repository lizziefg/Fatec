'''Exercício 3: Soma de Números Pares:
Peça um número e some apenas os números pares de 1 até ele.'''

n = int(input('Insira um número: '))

if n == 0 or n == 1:
    print('Não há números pares a serem somados.')
elif n != 0 or n != 1:
    soma = 0
    t = 1 #t indicará o número da tabuada por qual 2 será multiplicado

pares = n // 2 #a quantidade de números pares será a condição while

while pares != 0:
    soma += 2 * t
    pares -= 1
    t += 1

print('A soma dos números pares até ' + str(n) + ' será ' + str(soma))
