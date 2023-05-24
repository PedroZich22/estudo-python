"""Aula05 - Métodos especiais"""

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
       
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
 
    #__str__(self)
    # representação do objeto como string para humanos

    def __str__(self):
        return f'Retangulo[base={self.base}, altura={self.altura}]'
    

    #__repr__(self)
    # representação do objeto como string com o proposito de recriar esse objeto
    # logging, debug
    # representação caninoca
    def __repr__(self):
        return f'Retangulo({self.base, self.altura})'

retangulo1 = Retangulo(7.0, 5.0)
retangulo2 = Retangulo(8.0, 4.0)

representacao_string_reatangulo = 'Retangulo(7.0, 5.0)'
print(retangulo1.__repr__())

retangulo3 = eval('Retangulo(7.0, 5.0)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
