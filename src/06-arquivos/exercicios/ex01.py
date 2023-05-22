from ex03 import linha_para_dict

def carregar_dados_alunos(arquivo):
    """retorna uma tupla de dicionarios com os dados dos alunos"""

    lista = []
    for linha in arquivo.readlines():
        lista.append(linha_para_dict(linha, ['prontuario', 'nome', 'email']))

    # lista = []
    # for dado in dados:
    #     # adicionar, em forma de dicionario, cada item de cada lista em outra uma lista
    #     # "dado" percorre os 3 alunos, cada indice de "dado" uma é uma informação q é atribuida a uma chave
    #     # corrigindo erro de mostrar "\n" com strip()
    #     lista.append({"prontuario": dado[0], "nome": dado[1], "email": dado[2].strip()})

    return tuple(lista) # retornar lista final com dados da cada aluno em formato de tupla


with open("src/06-arquivos/exercicios/arquivo_de_dados", "r", encoding='UTF-8') as arquivo:  
    print(carregar_dados_alunos(arquivo)) # mostrar resultado da tupla
