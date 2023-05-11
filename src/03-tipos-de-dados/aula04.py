"""Aula 04 - dicionario"""

#   dict (dicionario) 
# chave-valor
# key é unica
# mutável

# criar um dict 
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

# acessar valor por chave
print(carro, type(carro))
print(carro["marca"])
print(carro.get("marca"))

# pegar todas as chaves
print(carro.keys())
print(carro.values())
print(carro.items()) #lista de tuplas

# verifica se a chave existe
print("marca" in carro)

# adicionar chave-valor de fomra dinamica

carro["cor"] = "Azul"
print("cor" in carro)
print(carro)

# remove a chave
marca = carro.pop("marca") #retorna o valor
print(marca)
print(carro)

# loop

for key in carro:
    print(key, carro[key], type(key))

for key in carro.keys():
    print(key)

for value in carro.values():
    print(value, type(value))

for key, value in carro.items():
    print(key, value)

# lista de dict

aluno1 = {
    "nome": "Joao",
    "email": "joao@email.com",
    "notas": [10.0, 6.5, 4.8, 3.8,]
}

aluno2 = {
    "nome": "Maria",
    "email": "maria@email.com",
    "notas": [10.0, 6.5, 4.8, 3.8,]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno["nome"], aluno["email"], aluno["notas"])
    for nota in aluno["notas"]:
        print(nota)

