'''Faça um programa que 
- solicite ao usuário que informe seu salário bruto
- identifique a faixa de imposto aplicável
- calcule e exiba o valor do imposto a ser pago
- se estiver na faixa isenta, exiba uma mensagem informando que não há imposto a pagar'''

salario_bruto = float(input('Informe o salário bruto: '))

if salario_bruto <= 2112.00:
    print('Não há imposto a pagar')
elif 2112.01 <= salario_bruto <= 2826.65:
    aliquota = 0.075
    deducao = 158.40
    imposto = (salario_bruto * aliquota) - deducao
    print(f'O imposto a pagar é R$ {imposto}.')
elif 2826.66 <= salario_bruto <= 3751.05:
    aliquota = 0.15
    deducao = 370.40
    imposto = (salario_bruto * aliquota) - deducao
    print(f'O imposto a pagar é R$ {imposto}.')
elif 3751.06 <= salario_bruto <= 4664.68:
    aliquota = 0.225
    deducao = 651.73
    imposto = (salario_bruto * aliquota) - deducao
    print(f'O imposto a pagar é R$ {imposto}.')
elif salario_bruto > 4664.68:
    aliquota = 0.275
    deducao = 884.96
    imposto = (salario_bruto * aliquota) - deducao
    print(f'O imposto a pagar é R$ {imposto}.')