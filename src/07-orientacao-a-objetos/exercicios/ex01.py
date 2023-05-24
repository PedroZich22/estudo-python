class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, value):
        if str(value) != "":
            self._prontuario = str(value)
        else:
            raise ValueError("O valor do prontuário não pode ser vazio")
    

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if str(value) != "":
            self._nome = str(value)
        else:
            raise ValueError("O valor do nome não pode ser vazio")
    

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if str(value) != "":
            self._email = str(value)
        else:
            raise ValueError("O valor do email não pode ser vazio")

    
    @classmethod
    def from_string(cls, string):
        prontuario, nome, email = string.split(sep=",")
        return cls(prontuario, nome, email)
    

    def __eq__(self, value):
        if(isinstance(value, self.__class__)):
            return self.prontuario == value.prontuario
        return False
    
    
aluno1 = Aluno.from_string('SP325, Pedro, pedro@email.com')
aluno2 = Aluno.from_string('SP325, Joao, joao@email.com')

print(aluno1.nome, aluno1.email, aluno1.prontuario)
print(aluno2.nome, aluno2.email, aluno2.prontuario)
print(aluno1 == aluno2)
