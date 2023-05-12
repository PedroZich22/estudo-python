"""Aula 01 - introdução a funções"""

# bloco de codigo que realiza alguma tarefa especifica
# dividir o problema em pequenas partes
# evita dupilicação de código

# 1. Standart Library Functions - built-in functions
# ex.: print, len

# 2.User Defined Functions 
# definidas  pelo desenvolvedor
# Fazer parte da solução do problema

# declarar funcao
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum
def saudacoes():
    print("Oi")

# chamada 
saudacoes()
saudacoes()
saudacoes()


# declarar funcao
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum

def saudacoes2(nome):
    print(f"Oi, {nome}")

# chamada
saudacoes2("Pedro")
nome = "Carlos"
saudacoes2(nome)


# declarar funcao
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: nenhum

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/ 3
    print(media)

# chamada 
#argumentos literais
calcular_media(10, 3, 7)

n1 = 3
n2 = 7
n3 = 7
#argumentos variaveis
calcular_media(n1, n2, n3)


# declarar funcao
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: a media

def calcular_media2(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/ 3
    return media

# chamada 
#argumentos literais
media = calcular_media(10, 3, 7)

n1 = 3
n2 = 7
n3 = 7
#argumentos variaveis
media = calcular_media(n1, n2, n3)
print(media)   
