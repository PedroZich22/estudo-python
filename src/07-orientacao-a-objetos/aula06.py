"""Aula 06 - equal e hash code"""

nome1 = 'Joao'
nome2 = 'Joao'

class Pessoa:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    
    # def __eq__(self, value):
    #     if isinstance(value, self.__class__):
    #         return self.cpf == value.cpf
    #     return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa(cpf={self.cpf}, nome={self.nome})'

pessoa1 = Pessoa('10001000-10', 'Joao')  
pessoa2 = Pessoa('10001000-10', 'Joao')  
pessoa3 = Pessoa('10001000-11', 'Maria')  

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)

print(pessoa1 == pessoa2)