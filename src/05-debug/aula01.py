"""Aula 1 - debug"""


def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma


def subtrair(n1, n2, n3):   
    subtracao = n1 - n2 - n3
    return subtracao


def calcular_media(n1, n2, n3):
    soma = somar(n1, n2, n3) - subtrair(n1, n2, n3)
    media = soma / 3
    return media


nota1 = 10.0
nota2 = 5.6
nota3 = 4.8


media = calcular_media(nota1, nota2, nota3)
print(media)
