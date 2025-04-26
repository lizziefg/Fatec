salario = int(input('Informe o valor do salário bruto: '))

if salario <= 1900:
    print('Alíquota de imposto de renda: isento')
elif 1900 < salario <= 2800:
    print('Alíquota de imposto de renda: 7.5%')
elif 2800 < salario <= 3700:
    print('Alíquota de imposto de renda: 15%')
elif 3700 < salario <= 4600:
    print('Alíquota de imposto de renda: 22.5%')
elif salario > 4600:
    print('Alíquota de imposto de renda: 27.5%')
