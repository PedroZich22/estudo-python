
"""Verifica se o codigo esta correto"""

codigo = input('Digite o código para avaliação: ')

if len(codigo) != 7:
    print( "Codigo invalido!")
elif codigo[:2] != "BR":
    print( "Codigo invalido!")
elif codigo[-1] != "X":
    print( "Codigo invalido!")
else:
    try:
        codigo = int(codigo[3:6])
        print("O codigo é valido!")
    except TypeError as erro:
        print("Codigo invalido!")
