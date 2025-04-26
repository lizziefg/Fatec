numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira outro número: '))

if numero1 > numero2:
    numero1=str(numero1)
    print(numero1 + ' é o maior número.')
elif numero2 > numero1:
    numero2=str(numero2)
    print(numero2 + ' é o maior número.')
elif numero1 == numero2:
    numero1=str(numero1)
    numero2=str(numero2)
    print(numero1 + ' e ' + numero2 + ' são iguais.')
