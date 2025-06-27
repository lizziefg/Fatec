'''Exercício 6 – Tupla de tuplas
Considere a seguinte tupla com informações de produtos:
Percorra os itens do carrinho e exiba uma lista com os produtos e seus preços, um por linha, no
formato:
Produto: Arroz | Preço: R$ 24.90'''

carrinho = (
    ('Arroz', 24.90),
    ('Feijão', 8.50),
    ('Leite', 4.80)
)

for itens in carrinho: #cada "itens" será uma tupla
  print(f'Produto: {itens[0]} | Preço: R$ {itens[1]}')