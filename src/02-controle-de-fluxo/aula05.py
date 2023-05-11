""" Aula 05 - break e continue"""

for i in range(10):
    if i == 4:
        break
    print(i)

# encontrar a posição de um numero em uma lista de inteiros
# se n encontrar = -1

busca = 5
numeros = [1, 4, 3, 2, 1, 5, 6, 7, 8]
posicao = -1

contador = 0
for numero in numeros:
    if numero == busca:
        posicao = contador
        break

    contador += 1

print(posicao)

# for i in range(len(numeros)):
#     if numeros[i] == busca:
#         posicao = i
#         break

# print(posicao)

# continue
#pular a iteração atual
print('----------')
for numero in numeros:
    if numero == 3:
        continue
    print(numero)

