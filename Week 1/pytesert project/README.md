# OCR PDF Converter

This project converts scanned or flattened PDFs into searchable PDFs using Python and OCR technology. It takes a PDF with image-based content, performs OCR (Optical Character Recognition) on each page, and outputs a new PDF file with embedded, searchable text. This is ideal for making scanned documents accessible for text-based searches.

## Features

- **OCR Conversion**: Converts scanned/flattened PDFs into searchable PDFs by extracting text from each page.
- **PDF Page to Image Conversion**: Uses `pdf2image` to convert PDF pages to images for OCR processing.
- **Text Embedding**: Embeds OCR-extracted text in the output PDF, making it searchable and selectable.
- **Automatic Cleanup**: Deletes temporary images created during the process to keep the project directory clean.

## Project Structure

OCR-PDF-Converter/ ├── .venv/ # (Optional) Virtual environment directory ├── app.py # Main Python script for OCR processing ├── otr1.pdf # Input PDF file (example scanned/flattened PDF) ├── out_text.pdf # Output PDF with searchable text ├── README.md # Project documentation └── requirements.txt # List of required Python packages


## Requirements

Ensure the following are installed:

- **Python 3.12**
- **Tesseract OCR Engine**: [Download Tesseract](https://github.com/tesseract-ocr/tesseract) and ensure it’s added to your system PATH.
- **Poppler**: Required by `pdf2image` for PDF-to-image conversion. [Download Poppler for Windows](https://blog.alivate.com.au/poppler-windows/), and add it to PATH.

### Python Libraries

Install the necessary Python packages in a virtual environment:

```bash
pip install pytesseract pdf2image reportlab pymupdf
```