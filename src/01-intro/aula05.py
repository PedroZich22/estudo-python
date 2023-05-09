""" Aula 05 - Tipos de dados"""

# numericos
# int, float

idade = 18
peso = 90.3

print(idade, type(idade))
print(peso, type(peso))

# string

nome = 'Pedro'
sobrenome = 'Zich'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca'

print(f'O cliente {nome} {sobrenome} comprou o {produto}')

print(nome[-1])
print(nome[0])

print(nome.upper())
print(nome.lower())

print(1, 3, 4, 5, sep='@')

# boolean
ligado = True
print(ligado, type(ligado))

resultado = 10 == 10
print(resultado, type(resultado)) 

# listas
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
# print(frutas[3]) index error

frutas[0] = 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# tuplas
codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])

print(len(codigos))

# conjuntos

resultado_sorteio = {10, 34, 54, 5, 43}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)

# dicionarios
funcionario = {
    'nome': 'João',
    'idade': 30,
    'salario': 5000
}

print(funcionario)
print(funcionario['nome'])
print(funcionario['idade'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())

funcionario['salario'] = 9000.9
print(funcionario)
