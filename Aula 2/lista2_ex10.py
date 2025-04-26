'''
Exercício 10: Criando uma mensagem personalizada
Peça ao usuário que digite um nome e um evento especial (por exemplo, "Festa de Aniversário").
Armazene essas informações e exiba a seguinte mensagem formatada:
"Olá, [nome]! Você está convidado(a) para a [evento]. Esperamos por você!"
'''
destinatario = input('Digite o nome do destinatário: ')
evento = input('Digite qual será o evento: ')
print('Olá, ' + destinatario + '! Você está convidado(a) para o/a ' + evento + '. Esperamos por você!')
