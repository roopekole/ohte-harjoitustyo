import PyPDF2

def parse_pdf(pdf):
    """

    Args:
        pdf: PDF document file from which text content is extracted

    Returns: Extracted text content

    """
    with open(pdf, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        full_content = ""
        for page_number in range(number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            full_content += page_content + "\n"
    return full_content
