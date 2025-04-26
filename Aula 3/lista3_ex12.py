temperatura = int(input('Informe a temperatura em Celsius: '))

if temperatura <= 15:
    print('Frio')
elif 16 <= temperatura <= 25:
    print('Agradável')
elif temperatura > 25:
    print('Quente')
