import pdfplumber


def extrair_texto(caminho):
    texto = ""
    with pdfplumber.open(caminho) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto


caminho = "./doc/doc.pdf"

texto = extrair_texto(caminho)

print(texto)
