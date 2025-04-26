lado1 = int(input('Insira um número representando um lado de um triângulo: '))
lado2 = int(input('Insira um número para o outro lado: '))
lado3 = int(input('Insira um número para o terceiro lado: '))

if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 ==lado3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
