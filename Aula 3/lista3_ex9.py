salario = int(input('Informe o salário atual: '))

if salario < 2000:
    bonus = "20%"
    salario_acrescido = salario * 1.2
elif 2000 <= salario < 5000:
    bonus = "10%"
    salario_acrescido = salario * 1.1
elif salario >= 5000:
    bonus = "5%"
    salario_acrescido = salario * 1.05

salario_acrescido = str(salario_acrescido)
print('Você recebe ' + bonus + '. Seu salário acrescido é R$ ' + salario_acrescido + '.')
