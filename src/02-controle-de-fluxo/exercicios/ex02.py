entrada = input('Digite as notas separadas por virgulas: ')

notas = entrada.split(sep=',')

notas = [float(nota) for nota in notas]

soma = 0.0
for nota in notas:
    soma += nota
    
media = soma / len(notas)

print(f'Sua média é: {media}')
