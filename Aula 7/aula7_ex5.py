'''Exercício 5 – Desempacotamento de tupla
Dada a tupla:
Desempacote a tupla em duas variáveis chamadas nome e preco, e depois exiba uma mensagem
formatada como:
O produto Arroz 5kg custa R$ 24.90.'''

produto = ('Arroz 5 kg', 24.90)

nome = produto[0]
preco = produto[1]

print(f'O produto {nome} custa R$ {preco}.')