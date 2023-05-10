""" Aula 02 - IF """

# if(condicao):
#     print('A condição é verdade')

codico_cliente = 32
valor_desconto = 12.0
DESCONTO_ESPECIAL = valor_desconto >= 20

if DESCONTO_ESPECIAL:
    print('Desconto especial')
    print(codico_cliente)
else:
    print('Não há desconto especial')
    
# EX: Nome com pelo menos 3 caracteres 
nome = 'Lo'

NOME_INVALIDO = len(nome) < 3

if not NOME_INVALIDO:  
    print('Nome válido')
else:
    print('Nome muito curto, deve ter pelo menos 3 caracteres')

NOME_VALIDO = len(nome) >= 3

if NOME_VALIDO:  
    print('Nome muito curto, deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')
    
# Nome com pelo menos 3 caracteres 
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas

nome = 'Lo'
idade = 17
erros = []

if NOME_INVALIDO:
    erros.append('Nome muito curto, deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade inválida, deve ser maior que 18')

# False: False, None, 0, 0.0, string vazia ''/ lista, tuple ou set vazio
# True: todo o reste

if erros:
    print(f'Erros:{erros}')
else:
    print('Nome e Idade válidos')

# if elif else

# Verifica se um numero é positivo ou negativo ou 0
numero = 3

if numero > 0:
    print('Número positivo')
elif numero == 0:
    print('Número igual a 0')
else:
    print('Número negativo')

# calcule a media e verifique se as duas notas são validas antes do calculo

n1 = 5.6
n2 = 10.0

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

# cuidado com ifs alinhados

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Nota 1 inválida')




