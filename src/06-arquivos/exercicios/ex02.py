def carregar_dados_alunos(arquivo):
    """retorna uma tupla de dicionarios com os dados dos alunos"""

    lista = []
    for linha in arquivo.readlines():
        dados = linha.split(',')
        lista.append({"codigo": int(dados[0]), "titulo": dados[1], "responsavel": dados[2].strip()})

    return tuple(lista) # retornar lista final com dados da cada aluno em formato de tupla


with open("src/06-arquivos/exercicios/arquivo_de_dados", "r", encoding='UTF-8') as arquivo:  
    tupla = carregar_dados_alunos(arquivo) # mostrar resultado da tupla
    print(tupla)