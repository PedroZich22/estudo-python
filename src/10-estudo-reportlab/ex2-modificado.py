from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Cria um objeto SimpleDocTemplate com o nome do arquivo e o tamanho da página
pdf_file = "ex2.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Obtém o estilo de folha de estilos de exemplo
styles = getSampleStyleSheet()

# Cria uma lista de elementos de conteúdo do PDF
content = []

# Adiciona um título com fonte 16pt
title_text = "<font size='16'>Título</font>"
title = Paragraph(title_text, styles["Heading1"])
content.append(title)

# Adiciona um espaço de 20pt após o título
content.append(Spacer(1, 20))

# Adiciona o primeiro parágrafo com fonte 12pt
paragraph1_text = "paragrafo1"
paragraph1 = Paragraph(paragraph1_text, styles["BodyText"])
content.append(paragraph1)

# Adiciona um espaço de 15pt entre os parágrafos
content.append(Spacer(1, 15))

# Adiciona o segundo parágrafo com fonte 12pt
paragraph2_text = "paragrafo2"
paragraph2 = Paragraph(paragraph2_text, styles["BodyText"])
content.append(paragraph2)

# Adiciona o terceiro parágrafo
estilo_parag_3 = ParagraphStyle(
    name="paragrafo3",
    fontSize = 16,
    alignment = 1,
    leading = 24
)

paragraph3_text = "paragrafo3"
paragraph3 = Paragraph(paragraph3_text, estilo_parag_3)
content.append(paragraph3)

doc.build(content)
