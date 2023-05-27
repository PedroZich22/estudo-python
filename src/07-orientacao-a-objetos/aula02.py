"""Aula 02 - Atributos de classe e instancia"""

# classe Pessoa possui:
# atributos de instancia : nome, email
# atributos de classe: humano
class Pessoa:
    especie = "humano"
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa(nome="Pedro", email="pedro@email.com")
pessoa2 = Pessoa(nome="Maria", email="maria@email.com")
 
# alterar atributo de classe na instancia (objeto)
# altera somente para aquela instancia
pessoa1.especie = "alienigena"

# alterando um atributo de classe na classe
# altera todos os objetos e na calsse tambem
Pessoa.especie = "alienigenas do passado"

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(Pessoa.especie)
