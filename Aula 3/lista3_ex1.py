numero = int(input('Digite um número inteiro: '))

if numero > 0:
    numero = str(numero)
    print(numero + ' é um número positivo.')
elif numero < 0:
    numero = str(numero)
    print(numero + ' é um número negativo.')
elif numero == 0:
    numero = str(numero)
    print(numero + ' é zero.')
