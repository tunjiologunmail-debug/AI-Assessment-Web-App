# Generates a professional PDF report using FPDF2.
# FPDF2 is pure Python — no external tools required.
 
from fpdf import FPDF
import datetime
 
 
class MaturityReportPDF(FPDF):
    """Custom PDF class with header and footer."""
 
    def __init__(self, institution_name):
        super().__init__()
        self.institution_name = institution_name
 
    def header(self):
        # Blue header bar
        self.set_fill_color(26, 58, 107)  # #1A3A6B
        self.rect(0, 0, 210, 18, 'F')
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(255, 255, 255)
        self.cell(0, 18, '  AI Maturity Assessment Report', align='L')
        self.ln(20)
 
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
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
    """
    Generates a PDF report and returns the file path.
 
    Parameters:
    -----------
    institution_name : Name shown on the report
    scores           : Dict of dimension scores
    report_text      : The GPT-4 generated markdown report
    output_path      : Where to save the PDF
    """
 
    pdf = MaturityReportPDF(institution_name)
    pdf.add_page()
 
    # Title section
    pdf.set_font('Helvetica', 'B', 22)
    pdf.set_text_color(26, 58, 107)
    pdf.cell(0, 12, 'AI Maturity Assessment Report', ln=True, align='C')
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(70, 70, 70)
    pdf.cell(0, 8, institution_name, ln=True, align='C')
    pdf.ln(8)
 
    # Score summary table
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_fill_color(234, 242, 251)
    pdf.set_text_color(26, 58, 107)
    pdf.cell(0, 8, 'Dimension Scores', ln=True, fill=True)
    pdf.ln(2)
 
    for dim, score in scores.items():
        # Score bar visualisation
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(90, 7, dim)
        # Draw score bar
        bar_width = (score / 5) * 80
        pdf.set_fill_color(46, 109, 164)
        pdf.rect(pdf.get_x(), pdf.get_y() + 1, bar_width, 5, 'F')
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(pdf.get_x() + bar_width, pdf.get_y() + 1, 80 - bar_width, 5, 'F')
        pdf.set_x(pdf.get_x() + 82)
        pdf.cell(18, 7, f'{score:.1f}/5', ln=True)
 
    pdf.ln(6)
 
    # Report content — parse markdown headings
    pdf.set_text_color(50, 50, 50)
    for line in report_text.split('\n'):
        if line.startswith('## '):
            pdf.ln(4)
            pdf.set_font('Helvetica', 'B', 12)
            pdf.set_text_color(26, 58, 107)
            pdf.cell(0, 8, line.replace('## ', ''), ln=True)
            pdf.set_font('Helvetica', '', 10)
            pdf.set_text_color(50, 50, 50)
            pdf.ln(2)
        elif line.startswith('- ') or line.startswith('* '):
            pdf.set_font('Helvetica', '', 10)
            pdf.cell(6, 6, chr(149))  # Bullet character
            pdf.multi_cell(0, 6, line[2:])
        elif line.strip():
            pdf.set_font('Helvetica', '', 10)
            pdf.multi_cell(0, 6, line)
            pdf.ln(1)
 
    pdf.output(output_path)
    return output_path
