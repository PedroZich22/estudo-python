def verificar_codigo(codigo):
    """Verifica se o codigo esta correto"""
    if len(codigo) != 7:
        return "Codigo invalido!"
    elif codigo[:2] != "BR":
        return "Codigo invalido!"
    elif codigo[-1] != "X":
        return "Codigo invalido!"
    else:
        try:
            codigo = int(codigo[3:6])
            return "O codigo é valido!"
        except:
            return "Codigo invalido!"
        

codigo = input('Digite o código para avaliação: ')

print(verificar_codigo(codigo))
