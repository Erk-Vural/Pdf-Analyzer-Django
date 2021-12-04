# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

from pdfminer import high_level

# Path of tesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

extracted_text = ""


def read_text():
    global extracted_text

    local_pdf_filename = '../static/Main/documents/example-2.pdf'
    pages = [0, 1]

    extracted_text = high_level.extract_text(local_pdf_filename, "", pages)

    if extracted_text == "":
        read_image()


def read_image():
    # Part 1 - Save all pages from pdf as jpg

    # Store all the pages of the PDF in a variable
    pages = convert_from_path('../static/Main/documents/example-2.pdf', 100,
                              poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:
        # Declaring filename for each page of PDF as JPG
        filename = "page_" + str(image_counter) + ".jpg"

        # Save the image of the page in system
        page.save(filename, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1

    # Part 2 - Recognizing text from the images using OCR

    # Variable to get count of total number of pages
    file_limit = image_counter - 1

    # Creating a text file to write the output
    outfile = "out_text.txt"

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    f = open(outfile, "a")

    # Iterate from 1 to total number of pages
    for i in range(1, file_limit + 1):
        filename = "page_" + str(i) + ".jpg"

        # Recognize the text as string in image using pytesseract
        text = str((pytesseract.image_to_string(Image.open(filename))))

        text = text.replace('-\n', '')

        # Finally, write the processed text to the file.
        f.write(text)

    # Close the file after writing all the text.
    f.close()


if __name__ == "__main__":
    read_text()
