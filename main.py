from fpdf import FPDF
import pandas as pd


def footHead(ln):
    pdf.ln(ln)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    pass


def addLines():
    i = 20
    while i < 270:
        pdf.line(10, i, 200, i)
        i = i + 10


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 19, 200, 19)
    addLines()

    #Set the footer
    footHead(ln=240)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.line(10, 19, 200, 19)
        addLines()
        #Set the header
        footHead(ln=0)

pdf.output("output.pdf")
