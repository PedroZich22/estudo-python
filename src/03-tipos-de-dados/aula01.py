"""Aula 01 - listas"""

#   listas
# ordenadas
# mutáveis
# indexáveis

nomes = ['Pedro', 'Joao', 'Maria']
print(nomes)

print(nomes[0])

print(nomes[0:2])
# print(nomes[:2])

print(nomes[1:])

# modificar elementos

nomes[0] = 'Pedro Zich'
nomes[1:] = ['Maria da Silva', 'Joao Souza']
print(nomes)

# tamanho da lista
# funcao len
print(len(nomes))

# adicionar elementos
# metodo append
nomes.append('Carlos')
print(nomes)

# metodo insert - em posicao especifica
nomes.insert(0, 'Guilherme')
print(nomes)

nomes.insert(2, 'Ana')
print(nomes)

# metodo extend - elemntos de outra lista
nomes2 = ["Caio", "Jonas"]
nomes.extend(nomes2)
print(nomes)

# remover elementos
# metodo remove
nomes.remove("Caio")
print(nomes)

# metodo del - remove da memoria
del nomes[0]

# metodo clear - limpar lista
# nomes.clear()

# iteração em listas
for nome in nomes:
    print(nome)

print('------')

for i in range(len(nomes)): 
    print(nomes[i])


