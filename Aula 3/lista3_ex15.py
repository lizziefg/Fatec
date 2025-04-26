idade = int(input('Informe a idade: '))
estudante = input('Informe se possui cartão estudante (S/N): ')

if idade <= 6 or idade >= 65:
    print('Tarifa de ônibus grátis')
elif estudante == "S":
    print('Tarifa de ônibus com 50% de desconto')
else:
    print('Tarifa normal')
