'''Faça um programa que
- solicite a idade do escoteiro
- verifique a categoria na qual se encaixa
- exiba na tela
- se o usuário digitar uma idade inválida (menor que 6 anos), exiba uma mensagem de erro'''

print('Categoria de escoteiro')
idade = int(input('Informe a idade: '))

if 6 <= idade <= 10:
    print('Lobinho')
elif 11 <= idade <= 14:
    print('Escoteiro')
elif 15 <= idade <= 17:
    print('Sênior')
elif 18 <= idade <= 21:
    print('Pioneiro')
elif idade > 21:
    print('Líder')
else:
    print('Erro. Informe uma idade igual ou maior a 6')