'''Exercício 7
Faça um programa que receba um valor N inteiro e positivo.
Este número indica quantos valores inteiros e positivos devem ser lidos a seguir.
Para cada número lido, mostre o valor e o cálculo fatorial deste número.'''

n = int(input('Informe um número inteiro e positivo: '))

for valor in range(n + 1, n + n + 1): # o range percorre os números seguintes
    print('Valor: ' + str(valor))
    fatorial = 1
    for f in range(1, valor+1):
        fatorial *= f # cálculo do fatorial
    print('Fatorial: ' + str(fatorial))