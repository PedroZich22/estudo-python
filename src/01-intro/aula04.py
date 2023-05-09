""" Aula 04 - constantes e literais """

# variavel - conteiner para guardar dados ou pnteiro
# inferenccia de tipo - dinamica

numero = 10
print(numero, type(numero))

# alterar o valor de uma variavel
numero = 20
print(numero)

# multplas atribuicoes
nome, idade, endereco = 'Pedro', 17, 'Rua das...'
print(nome, idade, endereco)

# atribui o mesmo valor para varias variaveis
nome1 = nome2 = nome3 = 'Pedro'
print(nome1, nome2, nome3)

nome2 = 'Joao'
print(nome1, nome2, nome3)

# padrao snake_case
nome_da_variavel = 'Pedro'

# padrao camel case
nomeDaVariavel = 'Pedro'

# constantes
# upper case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# literais

idade = 21
print(idade)
print(21)

# numericos

print(10, type(10))
print(10.4, type(10.4))

# string

print('Pedro', type('Pedro'))
print("Pedro", type("Pedro"))

# booleano
print(True, type(True))
print(False, type(False))

# none
print(None, type(None))

# colecoes

# lista(list)
numeros = [1, 3, 5]
print(numeros, type(numeros))

# tupla(tuple)
emails = ('pedro@email.com', 'maria@email.com')
print(emails, type(emails))

# conjunto(set)
nomes = {'maria', 'joao', 'pedro', 'maria'}
print(nomes, type(nomes))

# dicionario(dictionary)
aluno = {
    'nome': 'Pedro',
    'idade': 21,
    'email': 'pedro@email.com'
}

print(aluno, type(aluno))
