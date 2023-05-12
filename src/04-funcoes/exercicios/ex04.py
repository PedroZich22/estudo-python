def somar(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

resultado_soma = somar(1, 2, 3, 4, 5, 4)

print("A soma é: ", resultado_soma)
