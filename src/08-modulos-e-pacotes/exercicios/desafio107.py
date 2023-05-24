import moeda

valor = float(input('Digite o valor: R$'))

print(f'Metade do valor={moeda.metade(valor, True)}')
print(f'Dobro do valor={moeda.dobro(valor, True)}')
print(f'Aumento do valor={moeda.aumentar(valor, 10, True)}')
print(f'Diminuição do valor={moeda.diminuir(valor, 30, False)}')
