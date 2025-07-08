import pdfkit
import markdown2
import io
import os

# Optional: configure path to wkhtmltopdf (Windows only)
config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

def export_markdown(notes: str) -> str:
    return notes.strip()

def export_pdf(notes: str) -> bytes:
    # Convert markdown to HTML
    html = markdown2.markdown(notes)

    # Create in-memory output buffer
    pdf_output = io.BytesIO()

    # CSS path
    css_path = os.path.join(os.path.dirname(__file__), "pdf_style.css")
    if not os.path.exists(css_path):
        raise FileNotFoundError("Missing css file: pdf_style.css")

    # Convert HTML to PDF
    pdf_bytes = pdfkit.from_string(html, False, configuration=config, css=css_path)  # False returns bytes
    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)

    return pdf_output.read()
