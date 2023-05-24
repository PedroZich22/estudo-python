class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacao = []

    @classmethod
    def from_string(cls, string):
        codigo, titulo, responsavel = string.split(sep=",")
        return cls(int(codigo), string(titulo), string(responsavel))

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if value <= 0:
            self._codigo = value
        else:
            raise ValueError("O valor do código não pode ser vazio")
    

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if value != '':
            self._titulo = value
        else:
            raise ValueError("O valor do título não pode ser vazio")
    

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if value != '':
            self._responsavel = value
        else:
            raise ValueError("O valor do responsável não pode ser vazio")
        
    def add_participacao(self, participacao):
        self.participacao.append(participacao)

