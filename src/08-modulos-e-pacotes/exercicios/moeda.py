
def aumentar(valor, porcentagem, formatado):
    resultado = valor * (1 + (porcentagem/100))
    return formatar(resultado, formatado)

def diminuir(valor, porcentagem, formatado):
    resultado = valor * (1 - (porcentagem/100))
    return formatar(resultado, formatado)

def dobro(valor, formatado):
    resultado = valor * 2
    return formatar(resultado, formatado)

def metade(valor, formatado):
    resultado = valor / 2
    return formatar(resultado, formatado)

# 108
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

# 109
def formatar(resultado, formatado):
    if formatado:
        return moeda(resultado)
    return resultado