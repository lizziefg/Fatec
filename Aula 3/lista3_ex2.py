numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0 or numero == 0:
    numero = str(numero)
    print(numero + ' é um número par.')
elif numero % 2 != 0:
    numero = str(numero)
    print(numero + ' é um número ímpar.')
