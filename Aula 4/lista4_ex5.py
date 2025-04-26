'''Exercício 5:Cálculo do Fatorial
Escreva um programa em Python que solicite ao usuário um número inteiro n e calcule o fatorial desse número de duas formas:
Usando um laço for
Usando um laço while

Regras:
O usuário deve informar um número inteiro positivo (n ≥ 0). 
O programa deve exibir o resultado do fatorial calculado pelos dois métodos. 
O fatorial de 0 é 1, por definição.

Exemplo de entrada e saída esperada:
Digite um número para calcular o fatorial: 5
Usando for: 5! = 120
Usando while: 5! = 120

Dicas para resolver:
No laço for, utilize range() para iterar de 1 até n. 
No laço while, utilize uma variável auxiliar para multiplicação e outra para controlar a contagem.'''

n = int(input('Digite um número inteito positivo para calcular o fatorial: '))

if n == 0:
    ff = 1 #ff: fatorial "for"
    fw = 1 #fw: fatorial "while"

ff = 1
for i in range(1, n+1):
    ff *= i
print(f'Usando for: {n}! = {ff}') #fora do bloco para ser impresso apenas uma vez
           
fw = 1
i = 1
while i <= n:
    fw *= i
    i += 1
print(f'Usando while: {n}! = {fw}')
