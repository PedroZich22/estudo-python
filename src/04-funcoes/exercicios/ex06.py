def calcular_volume(comprimento, altura, largura):
    volume = (comprimento * altura * largura) / 1000
    return volume


def calcular_potencia_termostato(volume, temp_ambiente, temp_desejada):
    potencia_termostato = volume * 0.05 * (temp_desejada - temp_ambiente)
    return potencia_termostato


def quantidade_filtragem(volume):
    MIN_FILTRAGEM = int(volume * 2)
    MAX_FILTRAGEM = int(volume * 3)
    return f"{MIN_FILTRAGEM} a {MAX_FILTRAGEM}"

breakpoint()
comprimento = float(input("Digite o comprimento do aquario: "))
altura = float(input("Digite o altura do aquario: "))
largura = float(input("Digite o largura(cm) do aquario: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente: "))
temperatura_desejada = float(input("Digite a temperatura desejada: "))

volume = calcular_volume(comprimento, altura, largura)
potencia = calcular_potencia_termostato(volume, temperatura_ambiente, temperatura_desejada)
quantidade_filtragem = quantidade_filtragem(volume)

print(f"O volume do aquário é: {volume}")
print(f"A potencia do termostato deve ser: {potencia}")
print(f"A quantidade de filtragens deve ser no minimo de {quantidade_filtragem} vezes")

