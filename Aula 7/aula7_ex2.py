'''Exercício 2 – Itens exclusivos
Com os mesmos conjuntos:
Quais produtos apenas Maria comprou, e João não comprou?'''

joao = {"arroz", "feijão", "macarrão", "leite"}
maria = {"leite", "café", "açúcar", "arroz"}

print(maria.difference(joao))