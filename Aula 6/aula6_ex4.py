'''Faça um programa que solicite a idade do usuário e informe a condição para entrar em uma festa'''
print('Condições para a festa')
idade = int(input('Informe a idade: '))

if idade < 14:
    print('Não pode entrar na festa')
elif 14 <= idade < 18:
    print('Pode entrar com acompanhamento dos pais')
elif idade >= 18:
    print('Pode entrar')

if idade < 18:
    print('Não pode beber')
elif idade >= 18:
    print('Pode beber')