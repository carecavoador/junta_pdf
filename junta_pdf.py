"""
junta-pdf.py
versão 0.1.3
"""
import sys
from pathlib import Path
from datetime import datetime
from tkinter import messagebox

from PyPDF2 import PdfMerger, PdfReader


# Nome do novo PDF a ser criado.
novo_pdf = Path(f"junta_pdf_{datetime.now():%H_%M_%S}.pdf")

# PDFs a seres juntados passados como argumento.
lista_pdfs = [Path(p) for p in sys.argv[1:] if Path(p).suffix.lower() == ".pdf"]

def main():
    """Une os arquivos PDF passados por argumento em um único arquivo."""
    if not lista_pdfs:
        messagebox.showerror(
            title="Erro!",
            message="Nenhum arquivo PDF foi unido."
        )
        sys.exit()

    pdfs_juntos = PdfMerger()

    for arquivo in lista_pdfs:
        with open(arquivo, "rb") as file:
            novo = PdfReader(file)
            pdfs_juntos.append(novo)

    with open(novo_pdf, "wb") as pdf:
        pdfs_juntos.write(pdf)

    messagebox.showinfo(
        title="Concluído",
        message="PDFs unidos com sucesso!"
    )


if __name__ == "__main__":
    main()
