"""Aula 03 - loop for"""

# 1.repitir instruções
# 2.iteração em coleção de elementos

# nao da pra saber quantos elementos tem
linguagens = ['C', 'Pyhton', 'Java']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for (valor) in (coleção):
#     instrução

for linguagem in linguagens:
    print(linguagem.upper(), sep=', ')

# comportamento do "in" é diferente com base no contexto
print('Java' in linguagens)

nota1 = 10.0
nota2 = 8.3
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3
print(media)

notas = [10.0, 8.3, 7.5, 4.5]

soma = 0.0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(media)

# range
# valores = range(10)
# valores = range(0, 11, 2)
valores = range(10, 0, -1)
print(valores)

for valor in valores:
    print(valor)

# diferente forma usando range
for i in range(len(linguagens)):
    print(linguagem[i])
