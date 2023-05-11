codigo = input('Digite o código para avaliação: ')
erros = []

if 7 < len(codigo) > 7:
    erros.append('Código inválido! numero de caracteres insuficientes')

if codigo[0:2] == 'BR':
    erros.append('Nao comeca com "BR"')

if 1 > codigo[3:-1] > 9999:
    erros.append('Numero interno invalido')

if codigo[-1] != 'X':
    erros.append('Codigo invalido, ultimo digito diferente de "X"')
    
if erros:
    print('Codigo valido')
else:
    print(f'Erro(s) encontrado(s): {erros}')
