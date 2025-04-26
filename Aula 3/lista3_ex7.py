peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso/altura**2

if imc <= 18.5:
    imc=str(imc)
    print("O valor do IMC é " + imc + ". Classificação: abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    imc=str(imc)
    print("O valor do IMC é " + imc + ". Classificação: peso normal.")
elif imc >= 25 and imc <= 29.9:
    imc=str(imc)
    print("O valor do IMC é " + imc + ". Classificação: sobrepeso.")
elif imc >= 30 and imc <= 34.9:
    imc=str(imc)
    print("O valor do IMC é " + imc + ". Classificação: obesidade grau 1.")
elif imc >= 35 and imc <= 39.9:
    imc=str(imc)
    print("O valor do IMC é " + imc + ". Classificação: obesidade grau 2.")
elif imc >= 40:
    imc=str(imc)
    print("O valor do IMC é " + imc + ". Classificação: obesidade grau 3 (mórbida).")
