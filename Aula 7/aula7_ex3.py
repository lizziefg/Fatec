'''Exercício 3 – Lista sem repetição
Dada a seguinte lista de produtos (com duplicatas):
Crie um conjunto (set) a partir dessa lista para remover os itens repetidos e mostre os produtos únicos.'''

lista = ["arroz", "leite", "leite", "ovos", "ovos", "ovos", "açúcar", "farinha", "fermento", "manteiga", "fermento"]
únicos = set(lista)

print(únicos)