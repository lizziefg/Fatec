secreto = 33
numero = int(input('Tente adivinhar o número secreto: '))

if numero > secreto:
    print('Muito alto!')
elif numero < secreto:
    print('Muito baixo!')
elif numero == secreto:
    print('Parabéns!')
