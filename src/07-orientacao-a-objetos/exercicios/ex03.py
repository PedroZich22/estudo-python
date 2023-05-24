
from ex01 import Aluno

from ex02 import Projeto


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto


aluno1 = Aluno.from_string('SP325, Pedro, pedro@email.com')
aluno2 = Aluno.from_string('SP325, Joao, joao@email.com')

projeto1 = Projeto.from_string('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto2 = Projeto.from_string('2, Visão Computacional, Latorre')

projeto1.add_participacao(Participacao(1, '23/05/2023', '24/05/2023', aluno1, projeto1))
projeto2.add_participacao(Participacao(1, '23/05/2023', '24/05/2023', aluno2, projeto2))
