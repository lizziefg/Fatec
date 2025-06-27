'''Exercício 8
Faça um programa que calcule a soma dos primeiros 50 números pares.
Este programa não recebe valor do teclado. Os primeiros pares são: 2, 4, 6, ...'''

pares = 0
for i in range (0, 101, 2):
    pares += i
print(pares)