"""Aula 03 - set"""

#   set (conjunto) 
# nao sao ordenadas
# mutáveis
# nao indexável
# nao aceitam elementos duplicados

# criar um set 
numeros = {1 , 2 , 3 , 4 , 5 , 6 , 7}
print(numeros)

for numero in numeros:  
    print(numero)

print(3 in numeros)
print(90 in numeros)

# adicionar itens 
numeros.add(0)

# elementos de um set para outro

numeros2 = {1, 2, 3, 4}

numeros.update(numeros2)
todos_numeros = numeros.union(numeros2)

