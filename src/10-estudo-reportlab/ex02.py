from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Definindo o tamanho da página
page_size = letter

# Criando o documento PDF
pdf = SimpleDocTemplate("documento.pdf", pagesize=page_size)

# Obtendo os estilos de amostra
styles = getSampleStyleSheet()

# Criando uma lista para armazenar o conteúdo do documento
content = []

# Adicionando espaço entre o título e o primeiro parágrafo
espaco1 = Spacer(1, 15)
content.append(espaco1)

# Adicionando o título
title_text = "Título do Documento"
title = Paragraph(title_text, styles["Heading1"])
content.append([title, espaco1])

# Adicionando espaço entre os parágrafos
espaco2 = Spacer(1, 15)
content.append(espaco2)

# Adicionando o primeiro parágrafo
paragraph1_text = "Este é o primeiro parágrafo."
paragraph1 = Paragraph(paragraph1_text, styles["BodyText"])
content.append([paragraph1, espaco2])

# Adicionando o segundo parágrafo
paragraph2_text = "Este é o segundo parágrafo."
paragraph2 = Paragraph(paragraph2_text, styles["BodyText"])
content.append(paragraph2)

paragrafo_style = ParagraphStyle(
    name="paragrafo3",
    fontSize=12,
    leading=16,
    alignment=1
)

# Adicionando espaço entre os parágrafos
espaco3 = Spacer(1, 15)
content.append(espaco3)

# Adicionando o terceeiro parágrafo
paragraph3 = Paragraph("paragrafo 3", paragrafo_style)
content.append(paragraph3)

# Adicionando o conteúdo ao documento PDF
pdf.build(content)
