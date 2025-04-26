'''Faça um programa que:
- solicite ao usuário que informe o código do cargo,
- busque os valores correspondentes ao cargo na tabela e
- calcule o salário líquido com base na fórmula "salário líquido = salário base + benefícios - impostos" e
- exiba o salário líquido na tela'''

cargo = input('Informe o código do cargo: ')

if cargo == '1':
    salario_liquido = 2500 * 0.92 + 300
    cargo = 'Escriturário'
elif cargo == '2':
    salario_liquido = 3200 * 0.90 + 450
    cargo = 'Secretário'
elif cargo == '3':
    salario_liquido = 3800 * 0.88 + 600
    cargo = 'Caixa'
elif cargo == '4':
    salario_liquido = 7500 * 0.85 + 1000
    cargo = 'Gerente'
elif cargo == '5':
    salario_liquido = 12000 * 0.80 + 2000
    cargo = 'Diretor'

print(f'O salário líquido de {cargo} é R$ {salario_liquido}')