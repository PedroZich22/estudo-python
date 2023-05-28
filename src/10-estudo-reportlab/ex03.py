from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image

# Criação do arquivo PDF
pdf_file = "exemplo.pdf"
doc = SimpleDocTemplate(pdf_file)

# Definição dos estilos
titulo_style = {'fontName': 'Helvetica-Bold', 'fontSize': 16}
paragrafo_style = {'fontName': 'Helvetica', 'fontSize': 12}

# Conteúdo do documento
conteudo = []

imagem = Image()
imagem.drawWidth = 200
imagem.drawHeight = 200
conteudo.append(imagem)

# Título
titulo = "Título do Relatório"
titulo_texto = Paragraph(titulo, titulo_style)
conteudo.append(titulo_texto)
conteudo.append(Spacer(1, 20))  # Espaçamento de 20pt

# Parágrafo
paragrafo = "Este é um parágrafo de exemplo."
paragrafo_texto = Paragraph(paragrafo, paragrafo_style)
conteudo.append(paragrafo_texto)
conteudo.append(Spacer(1, 15))  # Espaçamento de 15pt

# Tabela
dados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    ["Dado 1", "Dado 2", "Dado 3", "Dado 4"]
]
tabela = Table(dados)
conteudo.append(tabela)

# Construção do PDF
doc.build(conteudo)
