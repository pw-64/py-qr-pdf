import qrcode
from fpdf import FPDF

# width and height of A4 page
pdf_w = 210
pdf_h = 297

# Creating of pdf class to perform operations
class PDF(FPDF):
    # Generating Qr code and saving in a folder.
    # Also adding a box and title to each QR
    def add_qr(self, text, x_offset, y_offset):
        img = qrcode.make("https://url/" + text, border=0)
        img.save("qrCodes/" + text + ".png")
        self.image("qrCodes/" + text + ".png", x=x_offset + 2, y=y_offset + 2.5, w=28, h=28)

        self.set_font('Arial', size=20)
        self.text(x=x_offset + 35, y=y_offset + 8, txt=text)
        self.set_font('Arial', size=15)
        self.text(x=x_offset + 35, y=y_offset + 18, txt="text 1")
        self.set_font('Arial', size=15)
        self.text(x=x_offset + 35, y=y_offset + 26, txt="text 2")
        self.set_font('Arial', size=12)
        self.text(x=x_offset + 2, y=y_offset + 36, txt="longer text")

    def add_header(self, text, x_offset, y_offset):
        self.set_font('Arial', size=15)
        self.text(x=x_offset + 35, y=y_offset + 8, txt=text)


pdf = PDF()
pdf.add_page()

# CONFIG
default_s1 = 4.0  # Margin from start of sheet
default_s2 = 12.0  # Margin from top of sheet
default_w = 99.1  # Width of each cell
default_h = 38.1  # Height of each cell
per_row :int = 2
rows_per_page :int = 7
pages :int = 3
start_barcode_at :int = 1

s1 = default_s1
s2 = default_s2
w = default_w
h = default_h

item_count = 0
page_count = 1
for i in range(start_barcode_at, start_barcode_at + per_row * rows_per_page * pages):
    pdf.add_qr(str(i), s1, s2)
    s1 = s1 + w + 3
    item_count += 1

    if item_count == 1: pdf.add_header("Designed to print on ... sticky labels", 10, 0)

    if item_count % per_row == 0:
        s1 = default_s1
        s2 = s2 + h + 1.6

    if (item_count % (per_row * rows_per_page) == 0) and (page_count != pages):
        page_count += 1
        pdf.add_page()
        s1 = default_s1
        s2 = default_s2
        w = default_w
        h = default_h
        item_count = 0

pdf.output('qr_codes.pdf', 'F')