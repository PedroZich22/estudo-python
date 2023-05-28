from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

# Criando um novo documento PDF
pdf = canvas.Canvas("hello_world.pdf", pagesize=letter)

# Definindo o tamanho da página
width, height = letter

# Escrevendo a string "Hello World" no documento PDF
pdf.setFont("Helvetica", 20)
pdf.drawString(50, height - 50, "Hello World")

# Desenhando algumas formas geométricas
pdf.setFillColor(colors.blue)
pdf.setStrokeColor(colors.red)
pdf.setLineWidth(2)

# Desenhando um retângulo
pdf.rect(50, height - 200, 200, 100, fill=True, stroke=True)

# Desenhando um círculo
pdf.circle(400, height - 150, 50, fill=True, stroke=True)

# Desenhando uma elipse
pdf.ellipse(400, height - 300, 100, 50, fill=True, stroke=True)

# Salvando o documento PDF
pdf.showPage()
pdf.save()
