compra = int(input('Informe o valor da compra: '))

if compra >= 100:
    compra = str(compra)
    print('Frete grátis. Total R$ ' + compra)
else:
    compra = compra + 15
    compra = str(compra)
    print('Frete de R$ 15. Total R$ ' + compra)
