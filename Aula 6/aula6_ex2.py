'''Faça um programa que mostre a data no formato por extenso.
O programa deve receber três números, representando dia, mês e ano, respectivamente'''

dia = input('Digite o dia: ')
mes = input('Digite o mês: ')
ano = input('Digite o ano: ')

if mes == '01':
    mes = 'janeiro'
elif mes == '02':
    mes = 'fevereiro'
elif mes == '03':
    mes = 'março'
elif mes == '04':
    mes = 'abril'
elif mes == '05':
    mes = 'maio'
elif mes == '06':
    mes = 'junho'
elif mes == '07':
    mes = 'julho'
elif mes == '08':
    mes = 'agosto'
elif mes == '09':
    mes = 'setembro'
elif mes == '10':
    mes = 'outubro'
elif mes == '11':
    mes = 'novembro'
elif mes == '12':
    mes = 'dezembro'

print('Data: ' + dia + ' de ' + mes + ' de ' + ano)