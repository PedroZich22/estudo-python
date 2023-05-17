def carregar_dados_alunos(arquivo):
    """retorna uma tupla de dicionarios com os dados dos alunos"""

    dados = []
    for linha in arquivo.readlines():
        # separação da separação dos dados do arquivo em uma lista
        # ou seja, dados = lista de 3 listas com 3 elementos, cada um sendo um dado do aluno
        dados.append(linha.split(','))

    lista = []
    for dado in dados:
        # adicionar, em forma de dicionario, cada item de cada lista em outra uma lista
        # "dado" percorre os 3 alunos, cada indice de "dado" uma é uma informação q é atribuida a uma chave
        # corrigindo erro de mostrar "\n" com strip()
        lista.append({"codigo": dado[0], "titulo": dado[1], "responsavel": dado[2].strip()})   

    return tuple(lista) # retornar lista final com dados da cada aluno em formato de tupla


with open("src/06-arquivos/exercicios/arquivo_de_dados", "r", encoding='UTF-8') as arquivo:  
    print(carregar_dados_alunos(arquivo)) # mostrar resultado da tupla
