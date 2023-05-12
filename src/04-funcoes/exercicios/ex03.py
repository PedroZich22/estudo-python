def somar(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

tupla = (2, 3, 4, 5)
resultado_soma = somar(tupla)
print(f"A soma dos numeros é: {resultado_soma}")
