'''Exercício 13 - "Alunos Matriculados"
Imprimir o nome de cada aluno e sua média.
Listar os alunos aprovados (média maior ou igual a 7.0).
Listar os alunos reprovados (média menor que 7.0).
Mostre os nomes em ordem alfabética em cada categoria.'''

boletim = {
    'Ana': (8.0, 7.5),
    'Carlos': (5.0, 6.0),
    'Beatriz': (9.0, 8.5),
    'Daniel': (6.0, 6.5)
}

print('Média dos alunos:')
for aluno in sorted(boletim):
  print(f'{aluno}: {sum(boletim[aluno])/2}')

print('Aprovados:')
for aluno in sorted(boletim):
  if sum(boletim[aluno])/2 >= 7:
    print(aluno)

print('Reprovados:')
for aluno in sorted(boletim):
  if sum(boletim[aluno])/2 < 7:
    print(aluno)