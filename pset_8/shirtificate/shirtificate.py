from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 30)
        self.cell(0, 30, "CS50 Shirtificate", align="C")


name = input("Name: ")

pdf = Shirtificate(orientation="P", format="A4")
pdf.add_page()
pdf.set_auto_page_break(False)

pdf.image("shirtificate.png", x=15, y=60, w=180)

pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(15, 140)
pdf.cell(180, 20, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
