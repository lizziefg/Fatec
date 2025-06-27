'''Exercício 8 – Adição e atualização
Com o mesmo dicionário tabela, faça o seguinte:
Adicione um novo item: "Café" com valor 14.20.
Atualize o preço do "Açúcar" para 4.10.
Imprima o dicionário atualizado.'''

tabela = {
    'Arroz': 24.90,
    'Feijão': 8.50,
    'Leite': 4.80,
    'Açúcar': 3.90
}

tabela.update({'Café': 14.20})
tabela['Açúcar'] = 4.10

print(tabela)