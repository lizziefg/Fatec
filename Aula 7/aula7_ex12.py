'''Exercício 12 - "Alunos Matriculados"
Você recebeu duas listas com os alunos matriculados em dois cursos diferentes. Cada aluno é
representado por uma tupla no formato:
(nome, matrícula)
Seu objetivo é:
Identificar os alunos que estão apenas no primeiro curso.
Identificar os alunos que estão apenas no segundo curso.
Identificar os alunos que estão matriculados nos dois cursos.'''

curso_a = {("Ana", 101), ("Carlos", 102), ("João", 103)}
curso_b = {("João", 103), ("Marina", 104), ("Carlos", 102)}

print('Alunos exclusivos do curso A:')
print(curso_a.difference(curso_b))

print('Alunos exclusivos do curso B:')
print(curso_b.difference(curso_a))

print('Alunos matriculados nos dois cursos:')
print(curso_a.intersection(curso_b))