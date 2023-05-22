def linha_para_dict(arquivo, lista):
    
    dados = []
    dados = arquivo.split(",")

    dicionario = {}
    for index, value in enumerate(lista):
        dicionario[value.strip()] = dados[index].strip()
    
    return dicionario

with open("src/06-arquivos/exercicios/arquivo_de_dados", "r", encoding='UTF-8') as arquivo: 
    # para leitura do arquivo
    linha = arquivo.readlines()[0]
    lista = ['prontuario', 'nome', 'email']

    resultado = linha_para_dict(linha, lista)
    print(resultado) # mostrar resultado do dicionario
