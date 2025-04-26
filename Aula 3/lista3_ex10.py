ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and not ano % 100 == 0) or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Não é bissexto.')

'''Para testes:
2000 é bissexto: divisível por 4, 100 e 400
1900 não bissexto: divisível por 4 e 100, não 400
2024 bissexto: divisível por 4
2025 não bissexto: não divisível por 4
1600 é bissexto: divisível por 4, 100 e 400'''
