'''Exercício 9 – Iteração sobre o dicionário
Use o dicionário:
Pergunta:
Percorra o dicionário e exiba cada item no formato:
Sabonete: R$ 2.50'''

compras = {
    'Sabonete': 2.50,
    'Shampoo': 15.00,
    'Condicionador': 16.50
}

for itens in compras:
  print(f'{itens}: R$ {compras[itens]}') #"itens" retornará as chaves e "compras[itens]" retornará os valores respectivos