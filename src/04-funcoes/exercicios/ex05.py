def calcular_imc(individuo):
    """retorna o imc de um indivíduo com base na sua altura e peso"""
    imc = individuo['peso'] / individuo['altura'] ** 2
    return imc


def obter_classificacao(imc):
    """retorna a classificação com base no imc"""
    if imc < 18.5:
        return "Baixo peso"
    if imc < 24.9:
        return "Peso normal"
    if imc < 29.9:
        return "Excesso de peso"
    if imc < 34.9:
        return "Obesidade de Classe 1"
    if imc < 39.9:
        return "Obesidade de Classe 2"
    if imc >= 40:
        return "Obesidade de Classe 3"


def situacao_individuo(imc):
    """ retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no imc"""
    if imc < 18.5:
        return "ganhar peso"
    if imc < 24.9:
        return "Peso normal"
    if imc >= 40:
        return "Perder peso"


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

individuo = {
    'altura': altura,
    'peso': peso
}

imc = calcular_imc(individuo)
print(f"Seu IMC é: {imc}")
print(f"Sua classificação é: {obter_classificacao(imc)}")
print(f"Sua situação é: {situacao_individuo(imc)}")
