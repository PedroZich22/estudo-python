def linha_para_dict(arquivo, lista):
    
    dados = []
    dados = arquivo.split(",")

    dicionario = {} 
    for i in range(len(lista)):  
        dicionario[lista[i].strip()] = dados[i].strip()

    # dicionario = {}
    # dicionario = {lista[0]: dados[0], lista[1]: dados[1], lista[2]: dados[2].strip('\n')}
    
    return dicionario

with open("src/06-arquivos/exercicios/arquivo_de_dados", "r", encoding='UTF-8') as arquivo: 
    # para leitura do arquivo
    arquivo = arquivo.readlines()[0]
    lista = ['prontuario', 'nome', 'email']

    resultado = linha_para_dict(arquivo, lista)
    print(resultado) # mostrar resultado do dicionario
