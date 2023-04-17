from fpdf import FPDF
import glob

filepaths = glob.glob("TheAnimals/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = filepath[11:len(filepath) - 4].title()
    with open(filepath, "r") as f:
        out = f.read()

    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=5, txt=f"{filename}", ln=1)
    pdf.set_font(family="Times", style="", size=8)
    pdf.cell(w=50, h=5, txt="", ln=2)
    pdf.multi_cell(0, 5, txt=out)

pdf.output(f"TheAnimals/TheAnimals.pdf")