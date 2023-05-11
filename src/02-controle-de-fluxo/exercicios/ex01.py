entrada = input('Digite as tres notas separadas por virgulas: ')

notas = entrada.split(sep=',')

notas = [float(nota) for nota in notas]

soma = 0.0
for nota in notas:
    soma += nota
    
media = soma / 3

print(f'Sua média é: {media}')
