idade = int(input('Informe a idade do atleta: '))

if idade <= 12:
    print('Categoria: infantil')
elif 12 < idade <= 17:
    print('Categoria: juvenil')
elif 17 < idade <= 40:
    print('Categoria: adulto')
elif idade > 40:
    print('Categoria: veterano')
