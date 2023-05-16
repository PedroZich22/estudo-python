# open("caminho", "r")

# Mode
# r - read
# a - append
# w - write
# x - criar arquivo
# r+ - write/read

arquivo = open("src/06-arquivos/test.txt", "r", encoding='utf-8')

print(arquivo.readable())

arquivo.close()
