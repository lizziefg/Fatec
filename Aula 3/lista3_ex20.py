idade = int(input('Informe a idade: '))
gestante = input('Informe se é gestante (S/N): ')
deficiente = input('Informe se é deficiente (S/N): ')

if idade >= 60 or deficiente == "S":
    print('Atendimento de prioridade máxima')
elif gestante == "S":
    print('Atendimento de prioridade média')
else:
    print('Atendimento normal')
