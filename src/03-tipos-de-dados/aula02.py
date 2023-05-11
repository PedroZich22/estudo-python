"""Aula 02 - tuplas"""

#   tuplas 
# ordenadas
# imutáveis
# indexável

# criação de tuplas
nomes = ("Pedro", "Joao", "Maria",)

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# iteração
for nome in nomes:
    print(nome)

# for i in range(len(nomes)):
#     print(nomes[i])

nomes2 = "Ana", "Marcos", "Gabriel"
print(nomes2)


# unpack
# nome1 = nomes2[0] 
# nome2 = nomes2[1] 
# nome3 = nomes2[2] 

nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)


# juntar tuplas 

todos_nomes = nomes + nomes2
print(todos_nomes)


