""" Aula 07 - I/0"""

# saida padrao - sys stdout
print('hello world!', 'Pedro', 1, True, sep='#', end='!!!!')
print('hello world!', 'Pedro', 1, True, sep='#', end='')

# arquivo = open('nomes.txt', 'w', encoding='utf-8')

print(
    'pedro@email.com', 
    'maria@email.com', 
    'joao@email.com', 
    file=arquivo,
    sep=';'
)

# entrada

nome = input("Digite o seu nome: ") 
idade = int(input("Digite sua idade: "))

# idade >= 18 ? print(f'{nome}, voce eh maior de idade') : print(f'{nome}, voce eh menor de idade')

# if(idade >= 18):
#     print(f'{nome}, voce eh maior de idade')
# else:
#     print(f'{nome}, voce eh menor de idade')

# file 
arquivos_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivos_notas.read()
notas = conteudo.split(sep=';')

notas = [float(nota) for nota in notas]
print(notas)

media = ((notas[0]) + (notas[1]) + (notas[2])) / len(notas)

print(media)


