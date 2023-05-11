
numeros = input("Digite 3 numeros separados por vigula: ")

numeros = [int(i) for i in numeros.split(",")]

menor = numeros[0]
maior = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
    if numero > maior:  
        maior = numero

print(f"O menor numero : {menor}\nO maior é: {maior} ")
