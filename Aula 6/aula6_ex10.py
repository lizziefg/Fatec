'''Exercício 10
Faça um programa que receba a idade e sexo ( M / F ) de dez alunos.
Esse programa deve apresentar quantos homens e quantas mulheres foram cadastrados.
Deve também calcular a média da idade dos homens, a média da idade das mulheres.'''

idade_homens = []
idade_mulheres = []

idade_aluno1 = int(input('Insira a idade do 1º aluno: '))
sexo_aluno1 = input('Informe o sexo do 1º aluno( M / F ): ')
if sexo_aluno1 == 'M':
    idade_homens.append(idade_aluno1)
else:
    idade_mulheres.append(idade_aluno1)

idade_aluno2 = int(input('Insira a idade do 2º aluno: '))
sexo_aluno2 = input('Informe o sexo do 2º aluno( M / F ): ')
if sexo_aluno2 == 'M':
    idade_homens.append(idade_aluno2)
else:
    idade_mulheres.append(idade_aluno2)

idade_aluno3 = int(input('Insira a idade do 3º aluno: '))
sexo_aluno3 = input('Informe o sexo do 3º aluno( M / F ): ')
if sexo_aluno3 == 'M':
    idade_homens.append(idade_aluno3)
else:
    idade_mulheres.append(idade_aluno3)

idade_aluno4 = int(input('Insira a idade do 4º aluno: '))
sexo_aluno4 = input('Informe o sexo do 4º aluno( M / F ): ')
if sexo_aluno4 == 'M':
    idade_homens.append(idade_aluno4)
else:
    idade_mulheres.append(idade_aluno4)

idade_aluno5 = int(input('Insira a idade do 5º aluno: '))
sexo_aluno5 = input('Informe o sexo do 5º aluno( M / F ): ')
if sexo_aluno5 == 'M':
    idade_homens.append(idade_aluno5)
else:
    idade_mulheres.append(idade_aluno5)

idade_aluno6 = int(input('Insira a idade do 6º aluno: '))
sexo_aluno6 = input('Informe o sexo do 6º aluno( M / F ): ')
if sexo_aluno6 == 'M':
    idade_homens.append(idade_aluno6)
else:
    idade_mulheres.append(idade_aluno6)

idade_aluno7 = int(input('Insira a idade do 7º aluno: '))
sexo_aluno7 = input('Informe o sexo do 7º aluno( M / F ): ')
if sexo_aluno7 == 'M':
    idade_homens.append(idade_aluno7)
else:
    idade_mulheres.append(idade_aluno7)

idade_aluno8 = int(input('Insira a idade do 8º aluno: '))
sexo_aluno8 = input('Informe o sexo do 8º aluno( M / F ): ')
if sexo_aluno8 == 'M':
    idade_homens.append(idade_aluno8)
else:
    idade_mulheres.append(idade_aluno8)

idade_aluno9 = int(input('Insira a idade do 9º aluno: '))
sexo_aluno9 = input('Informe o sexo do 9º aluno( M / F ): ')
if sexo_aluno9 == 'M':
    idade_homens.append(idade_aluno9)
else:
    idade_mulheres.append(idade_aluno9)

idade_aluno10 = int(input('Insira a idade do 10º aluno: '))
sexo_aluno10 = input('Informe o sexo do 10º aluno( M / F ): ')
if sexo_aluno10 == 'M':
    idade_homens.append(idade_aluno10)
else:
    idade_mulheres.append(idade_aluno10)

sexo_alunos = [sexo_aluno1, sexo_aluno2, sexo_aluno3, sexo_aluno4, sexo_aluno5, sexo_aluno6, sexo_aluno7, sexo_aluno8, sexo_aluno9, sexo_aluno10]
homens = sexo_alunos.count('M')
mulheres = sexo_alunos.count('F')
print('Foram cadastrados ' + str(homens) + ' homens e ' + str(mulheres) + ' mulheres.')

média_homens = 0
for h in idade_homens:
    média_homens += h
print('A média da idade dos homens é ' + str(média_homens/homens))

média_mulheres = 0
for m in idade_mulheres:
    média_mulheres += m
print('A média da idade das mulheres é ' + str(média_mulheres/mulheres))