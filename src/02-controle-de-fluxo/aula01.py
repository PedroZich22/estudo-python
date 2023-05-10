"""Aula 01 - operadores"""

# operadores aritmeticos

n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.4

print('1 + 1 =', 1 + 1, type(1+1))
print('1.2 + 1.3 =', 1.2 + 1.3, type(1.2+1.3))
print('resultado', resultado, type(resultado))
print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3 % 2)
print(10 // 3)
print(10 ** 2)

# atribuicao

x = 10.0
print(x)

# comparacao ou relacionais(bool)

resultado = x > 10
print(resultado, type(resultado))

print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 < 10', 10 < 10, type(10 < 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))

# logicos

print('True and True =', True and True, type(True and True))
print('True and False =', True and False, type(True and False))
print('False and True =', False and True, type(False and True))
print('False and False =', False and False, type(False and False))

print('True or True =', True or True, type(True or True))
print('True or False =', True or False, type(True or False))
print('False or True =', False or True, type(False or True))
print('False or False =', False or False, type(False or False))

condicao = True
print('not condicao =', not condicao, type(not condicao))

# especias

# is
# == comparar igualdade
# is comparar se as variaveis apontam para o mesmo objeto em memoria

a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c)

# in
# str, list, tuple, set, dic (chave)

frase = 'Voce eh um palavrao!'

print('palavrao' in frase)

numeros = [1, 5, 2, 6]
print(1 in numeros)

numeros = (1, 5, 2, 6)
print(1 in numeros)

numeros = {1, 5, 2, 6}
print(1 in numeros)

pessoa = {
    'nome': 'Pedro',
    'idade': 25,
    'sexo': 'M'
}

print('nome' in pessoa)
