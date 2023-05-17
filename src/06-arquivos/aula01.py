# open("caminho", "r")

# Mode
# r - read
# a - append
# w - write
# x - criar arquivo
# r+ - write/read

# arquivo = open("src/06-arquivos/test3.txt", "x", encoding='utf-8')

# READ

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)
# print(lista[2])

# APPEND

# arquivo.write("Python\n")

# arquivo.close()

import os 

# if os.path.exists("src/06-arquivos/test2.txt"):
#     os.remove("src/06-arquivos/test2.txt")
# else:
#     print("Arquivo não existe")

os.rmdir("src/06-arquivos/nova_pasta")
