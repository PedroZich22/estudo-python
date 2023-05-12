"""Aula 02 - Arguments: positional, keyword, default value"""

#declara um finção que soma dois numeros
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo/divisor


# argumentos posicionais
print(somar(10, 3.6))
print(somar(2.9, 7.6))
print(dividir(10, 2))


# argumentos nomeados (keyword)
print(somar(n1=3.0, n2=4.6))
print(somar(n2=7.0, n1=3.6))
print(dividir(divisor=3, dividendo=10))


# unpack list e tuplas 
numeros = [10.4, 3]
print("somar numeros de uma lista: ", somar(numeros[0], numeros[1]))
print("somar numeros de uma lista: ", somar(*numeros)) # unpack(tirar valores da lista)
# funciona com tupla tambem


# unpack de dict
numeros2 = {
    'n1' = 10.3,
    'n2' = 2.8
}

print("somar numeros de um dict: ", somar(**numeros2)) 
# precisa de 2 art para acessar o valor/key exatamente igual o parametro q ta na funcao

# Declaração
# nome: saudações
# parametros: nome(obrigatorio), saudação
# retorno: string 
def saudacoes(nome, saudacao="Oi"):
    return f"{saudacao} {nome}"

print(saudacoes("Pedro" "Olá"))
print(saudacoes("Maria" "Bom dia"))
print(saudacoes("Joao"))

print(saudacoes(saudacao="OI OI", nome="Marcia"))
print(saudacoes(nome="Jorge"))