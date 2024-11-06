import pytesseract
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

PDF_file = r"otr1.pdf"

def pdf_text():
    pages = convert_from_path(PDF_file, 500)
    image_counter = 1
    filelimit = len(pages)

    outfile = "output.pdf"

    with open(outfile, "wb") as f:  # Open output file in binary write mode
        for page in pages:
            # Save the image of the page in system
            filename = "page_" + str(image_counter) + ".jpg"
            page.save(filename, 'JPEG')

            # Perform OCR and get PDF as result
            result = pytesseract.image_to_pdf_or_hocr(filename, lang="eng")
            f.write(bytearray(result))

            # Increment counter and clean up image file
            image_counter += 1
            os.remove(filename)  # Clean up the temporary image file

pdf_text()
