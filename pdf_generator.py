# Generates a professional PDF report using FPDF2.
# FPDF2 is pure Python — no external tools required.

from fpdf import FPDF
import datetime
import os

# DejaVu fonts ship with matplotlib and support full Unicode
# (en dash, em dash, smart quotes, bullets, etc.)
_FONT_DIR = os.path.join(
    os.path.dirname(__import__('matplotlib').__file__),
    'mpl-data', 'fonts', 'ttf'
)
_FONT_REGULAR = os.path.join(_FONT_DIR, 'DejaVuSans.ttf')
_FONT_BOLD    = os.path.join(_FONT_DIR, 'DejaVuSans-Bold.ttf')
_FONT_ITALIC  = os.path.join(_FONT_DIR, 'DejaVuSans-Oblique.ttf')


class MaturityReportPDF(FPDF):
    """Custom PDF class with header and footer."""

    def __init__(self, institution_name):
        super().__init__()
        self.institution_name = institution_name
        # Register DejaVu as a Unicode-capable font family
        self.add_font('DejaVu', '',  _FONT_REGULAR, uni=True)
        self.add_font('DejaVu', 'B', _FONT_BOLD,    uni=True)
        self.add_font('DejaVu', 'I', _FONT_ITALIC,  uni=True)

    def header(self):
        self.set_fill_color(26, 58, 107)
        self.rect(0, 0, 210, 18, 'F')
        self.set_font('DejaVu', 'B', 11)
        self.set_text_color(255, 255, 255)
        self.cell(0, 18, '  AI Maturity Assessment Report', align='L')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 8)
        self.set_text_color(150, 150, 150)
        date_str = datetime.date.today().strftime('%B %Y')
        self.cell(0, 10,
            f'{self.institution_name}  |  AI Maturity Assessment  |  {date_str}  |  Page {self.page_no()}',
            align='C')


def generate_pdf_report(
    institution_name: str,
    scores: dict,
    report_text: str,
    output_path: str = '/tmp/maturity_report.pdf'
) -> str:
    pdf = MaturityReportPDF(institution_name)
    pdf.add_page()

    # Title section
    pdf.set_font('DejaVu', 'B', 22)
    pdf.set_text_color(26, 58, 107)
    pdf.cell(0, 12, 'AI Maturity Assessment Report', ln=True, align='C')
    pdf.set_font('DejaVu', '', 14)
    pdf.set_text_color(70, 70, 70)
    pdf.cell(0, 8, institution_name, ln=True, align='C')
    pdf.ln(8)

    # Score summary table
    pdf.set_font('DejaVu', 'B', 11)
    pdf.set_fill_color(234, 242, 251)
    pdf.set_text_color(26, 58, 107)
    pdf.cell(0, 8, 'Dimension Scores', ln=True, fill=True)
    pdf.ln(2)

    for dim, score in scores.items():
        pdf.set_font('DejaVu', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(90, 7, dim)
        bar_width = (score / 5) * 80
        pdf.set_fill_color(46, 109, 164)
        pdf.rect(pdf.get_x(), pdf.get_y() + 1, bar_width, 5, 'F')
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(pdf.get_x() + bar_width, pdf.get_y() + 1, 80 - bar_width, 5, 'F')
        pdf.set_x(pdf.get_x() + 82)
        pdf.cell(18, 7, f'{score:.1f}/5', ln=True)

    pdf.ln(6)

    # Report content - parse markdown headings
    pdf.set_text_color(50, 50, 50)
    for line in report_text.split('\n'):
        if line.startswith('## '):
            pdf.ln(4)
            pdf.set_font('DejaVu', 'B', 12)
            pdf.set_text_color(26, 58, 107)
            pdf.cell(0, 8, line.replace('## ', ''), ln=True)
            pdf.set_font('DejaVu', '', 10)
            pdf.set_text_color(50, 50, 50)
            pdf.ln(2)
        elif line.startswith('- ') or line.startswith('* '):
            pdf.set_font('DejaVu', '', 10)
            pdf.cell(6, 6, '\u2022')
            pdf.multi_cell(0, 6, line[2:])
        elif line.strip():
            pdf.set_font('DejaVu', '', 10)
            pdf.multi_cell(0, 6, line)
            pdf.ln(1)

    pdf.output(output_path)
    return output_path