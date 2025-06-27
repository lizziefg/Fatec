'''Exercício 9
Faça um programa que receba duas notas de seis alunos e calcule a média de cada aluno.
Para cada aluno, classifique-o conforme a tabela abaixo, mostrando a condição do aluno.
Média do Aluno | Condição do aluno
até 3,0 | Reprovado
Entre 3,0 e 7,0 | Exame
Acima de 7,0 | Aprovado'''

aluno1_nota1 = int(input('Insira a primeira nota do primeiro aluno: '))
aluno1_nota2 = int(input('Insira a segunda nota do primeiro aluno: '))
média_aluno1 = (aluno1_nota1+aluno1_nota2)/2
if média_aluno1 < 3:
    print('Reprovado')
elif 3 <= média_aluno1 <= 7:
    print('Exame')
elif média_aluno1 > 7:
    print('Aprovado')

aluno2_nota1 = int(input('Insira a primeira nota do segundo aluno: '))
aluno2_nota2 = int(input('Insira a segunda nota do segundo aluno: '))
média_aluno2 = (aluno2_nota1+aluno2_nota2)/2
if média_aluno2 < 3:
    print('Reprovado')
elif 3 <= média_aluno2 <= 7:
    print('Exame')
elif média_aluno2 > 7:
    print('Aprovado')

aluno3_nota1 = int(input('Insira a primeira nota do terceiro aluno: '))
aluno3_nota2 = int(input('Insira a segunda nota do terceiro aluno: '))
média_aluno3 = (aluno3_nota1+aluno3_nota2)/2
if média_aluno3 < 3:
    print('Reprovado')
elif 3 <= média_aluno3 <= 7:
    print('Exame')
elif média_aluno3 > 7:
    print('Aprovado')

aluno4_nota1 = int(input('Insira a primeira nota do quarto aluno: '))
aluno4_nota2 = int(input('Insira a segunda nota do quarto aluno: '))
média_aluno4 = (aluno4_nota1+aluno4_nota2)/2
if média_aluno4 < 3:
    print('Reprovado')
elif 3 <= média_aluno4 <= 7:
    print('Exame')
elif média_aluno4 > 7:
    print('Aprovado')

aluno5_nota1 = int(input('Insira a primeira nota do quinto aluno: '))
aluno5_nota2 = int(input('Insira a segunda nota do quinto aluno: '))
média_aluno5 = (aluno5_nota1+aluno5_nota2)/2
if média_aluno5 < 3:
    print('Reprovado')
elif 3 <= média_aluno5 <= 7:
    print('Exame')
elif média_aluno5 > 7:
    print('Aprovado')

aluno6_nota1 = int(input('Insira a primeira nota do sexto aluno: '))
aluno6_nota2 = int(input('Insira a segunda nota do sexto aluno: '))
média_aluno6 = (aluno6_nota1+aluno6_nota2)/2
if média_aluno6 < 3:
    print('Reprovado')
elif 3 <= média_aluno6 <= 7:
    print('Exame')
elif média_aluno6 > 7:
    print('Aprovado')