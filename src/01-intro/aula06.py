""" Aula 06 - conversao de tipos """
# linguagem tipagem forte
#conversao de tipo implicita

leitura = 5.34
peso = 3
total = leitura * peso
print(total, type(total))

# explicita (casting)

soma = 12.4 + float('3')
print(soma, type(soma))

idade = int('18')
print(idade, type(idade))

nome = 'Pedro'
altura = 1.75

# mensagem = nome + ' tem a altura de ' + str(altura)
mensagem = f'{nome} tem a altura de {altura}'
print(mensagem)

