from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Definindo o tamanho da página
page_size = letter

# Criando o documento PDF
pdf = SimpleDocTemplate("documento.pdf", pagesize=page_size)

# Obtendo os estilos de amostra
styles = getSampleStyleSheet()

# Definindo o estilo do título
title_style = styles["Title"]
title_style.fontSize = 16

# Definindo o estilo dos parágrafos
paragraph_style = styles["Normal"]
paragraph_style.fontSize = 12

# Criando uma lista para armazenar o conteúdo do documento
content = []

# Adicionando o título
title_text = "Título do Documento"
title = Paragraph(title_text, title_style)
content.append(title)

# Adicionando espaço entre o título e o primeiro parágrafo
espaco1 = Spacer(1, 15)

# Adicionando o primeiro parágrafo
paragraph1_text = "Este é o primeiro parágrafo."
paragraph1 = Paragraph(paragraph1_text, paragraph_style)
content.append(paragraph1)

# Adicionando espaço entre os parágrafos
espaco2 = Spacer(1, 15)

# Adicionando o segundo parágrafo
paragraph2_text = "Este é o segundo parágrafo."
paragraph2 = Paragraph(paragraph2_text, paragraph_style)
content.append(paragraph2)

paragrafo_style = ParagraphStyle(
    "paragrafo",
    fontName='Arial',
    fontSize=12,
    leading=16,
    alignment=1
)

# Adicionando espaço entre os parágrafos
espaco3 = Spacer(1, 15)

# Adicionando o terceeiro parágrafo
paragraph3 = Paragraph("paragrafo 3", paragrafo_style, espaco3)
content.append(paragraph3)


# Adicionando o conteúdo ao documento PDF
pdf.build(content)
