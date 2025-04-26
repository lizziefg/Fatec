'''Faça um programa que receba três notas, calcule e mostra a média ponderada e o conceito'''
trabalho_laboratorio = float(input('Digite a nota do Trabalho de Laboratório: '))
avaliacao_semestral = float(input('Digite a nota da Avaliação Semestral: '))
exame_final = float(input('Digite a nota do Exame Final: '))

nota_ponderada = (trabalho_laboratorio * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10
print(f'A nota ponderada é {nota_ponderada}')

if 8.0 <= nota_ponderada <= 10.0:
    print('Conceito A')
elif 7.0 <= nota_ponderada <= 7.9:
    print('Conceito B')
elif 6.0 <= nota_ponderada <= 6.9:
    print('Conceito C')
elif 5.0 <= nota_ponderada <= 5.9:
    print('Conceito D')
elif 0.0 <= nota_ponderada <= 4.9:
    print('Conceito E')