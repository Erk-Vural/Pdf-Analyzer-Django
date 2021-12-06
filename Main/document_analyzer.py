# -*- coding: utf-8 -*-
import os.path

from Main.Services.author import create_author
from Main.Services.course_name import create_course_name
from Main.Services.jury import create_jury_info
from Main.Services.keyword import create_keyword
from Main.Services.mentor import create_mentor_info
from Main.Services.semester import create_semester
from Main.Services.summary import create_summary
from Main.Services.title import create_title

import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from pdfminer import high_level

# Path of tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

filename = ""
user_id = 0
doc_id = 0

course_name = ""
title = ""
staff_info_block = ["", "", ""]
semester = ""
authors_info_block = ["", "", ""]
summary = ""
keywords = []

BASE = os.path.dirname(os.path.abspath(__file__))


def read_text(pages):
    local_pdf_filename = '../static/Main/documents/' + filename

    extracted_text = high_level.extract_text(os.path.join(BASE, local_pdf_filename), "", pages)

    return extracted_text


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


def read_course_name():
    global course_name

    pages = [1]
    extracted_text = read_text(pages)

    if extracted_text.find('BİTİRME ÇALIŞMASI') != -1:
        course_name = 'BİTİRME ÇALIŞMASI'

    elif extracted_text.find('ARAŞTIRMA PROBLEMLERİ') != -1:
        course_name = 'ARAŞTIRMA PROBLEMLERİ'

    create_course_name(user_id, doc_id, course_name)


def read_title():
    global title
    pages = [1]

    extracted_text = read_text(pages)

    # add 4 to avoid new lines
    start_point = extracted_text.find(course_name) + len(course_name) + 4

    block = extracted_text[start_point:]

    end_point = block.find("\n")

    title = block[: end_point]

    create_title(user_id, doc_id, title)


def read_staff():
    pages = [1]

    extracted_text = read_text(pages)

    start_point = extracted_text.find(title) + len(title) + 2

    block = extracted_text[start_point:]

    start_point = block.find("\n") + 2

    block = block[start_point:]

    block = block.replace("\n", "  ")
    block = block.replace("...", "")
    block = block.replace("..", "")
    block = block.replace("Kocaeli Üniv.", "")
    end_point = block.find("Tezin") - 5
    block = block[:end_point]

    end_point = block.find(",")
    staff_info_block[0] = block[:end_point]
    block = block[end_point + 4:]

    end_point = block.find(",")
    staff_info_block[1] = block[3:end_point]
    block = block[end_point + 4:]

    staff_info_block[2] = block

    for i in range(3):
        title_str = ""
        name_str = ""
        last_name_str = ""
        duty_str = ""

        while staff_info_block[i].find(".") != -1:
            point = staff_info_block[i].find(".")
            title_str = title_str + staff_info_block[i][:point]
            staff_info_block[i] = staff_info_block[i][point + 1:]

        if staff_info_block[i].find("Danışman") != -1:
            point = staff_info_block[i].find("Danışman")
            staff_info_block[i] = staff_info_block[i][:point]
            duty_str = "Danışman"

        elif staff_info_block[i].find("Jüri") != -1:
            point = staff_info_block[i].find("Jüri Üyesi")
            staff_info_block[i] = staff_info_block[i][:point - 1]
            duty_str = "Jüri Üyesi"

        staff_info_block[i] = staff_info_block[i][1:]

        point = staff_info_block[i].find(" ")
        name_str = staff_info_block[i][:point]
        last_name_str = staff_info_block[i][point + 1:]

        if duty_str == "Danışman":
            pass
            create_mentor_info(user_id, doc_id, name_str, last_name_str, title_str)
        create_jury_info(user_id, doc_id, name_str, last_name_str, title_str)


def read_semester():
    global semester

    pages = [1]
    extracted_text = read_text(pages)

    start_point = extracted_text.find("Tarih: ") + 7
    end_point = start_point + 10
    semester_str = extracted_text[start_point:end_point]

    month = int(semester_str[4])
    year = int(semester_str[6:])

    if month >= 3:
        semester = str(year - 1) + "-" + str(year) + " Bahar"
    else:
        semester = str(year) + "-" + str(year + 1) + " Güz"

    create_semester(user_id, doc_id, semester)


def read_author():
    global authors_info_block
    pages = [3]

    extracted_text = read_text(pages)

    for i in range(3):
        if extracted_text.find("Öğrenci") != -1:
            start_point = extracted_text.find("Öğrenci")
            end_point = extracted_text.find("İmza")

            authors_info_block[i] = extracted_text[start_point:end_point]

            extracted_text = extracted_text[end_point + 5:]

            start_point = authors_info_block[i].find("No:") + 4
            end_point = authors_info_block[i].find("Adı") - 1
            student_num = authors_info_block[i][start_point:end_point]

            start_point = authors_info_block[i].find("Soyadı:") + 8
            end_point = authors_info_block[i].find("İmza")
            name_last_name = authors_info_block[i][start_point:end_point]
            name_last_name = name_last_name.replace("\n", "")

            point = name_last_name.find(" ")
            name = name_last_name[0:point]
            last_name = name_last_name[point:]

            create_author(user_id, doc_id, name, last_name, student_num, "1")


def read_summary():
    global summary
    pages = [6, 7, 8, 9, 10, 11]

    extracted_text = read_text(pages)

    start_point = extracted_text.find("ÖZET") + 4
    end_point = extracted_text.find("Anahtar Kelimeler:") - 2
    extracted_text = extracted_text[start_point:end_point]
    summary = extracted_text.replace("\n", " ")

    create_summary(user_id, doc_id, summary)


def read_keywords():
    global keywords
    # range is wider for decrease missing wanted part of data
    pages = [6, 7, 8, 9, 10, 11]

    extracted_text = read_text(pages)

    start_point = extracted_text.find("Anahtar Kelimeler:") + 19
    extracted_text = extracted_text[start_point:]
    end_point = extracted_text.find("\n")
    keywords_str = extracted_text[:end_point]

    while keywords_str.find(",") != -1:
        point = keywords_str.find(",") + 2
        keyword = keywords_str[:point - 3]
        keywords_str = keywords_str[point:]

        keywords.append(keyword)

    # Get last keyword
    if keywords_str.find(",") == -1 and keywords_str != "":
        keyword = keywords_str

        keywords.append(keyword)

    for i in range(len(keywords)):
        pass
        create_keyword(user_id, doc_id, keywords[i])


def analyze_document(fl, u_id, d_id):
    global filename
    global user_id
    global doc_id

    filename = fl
    user_id = u_id
    doc_id = d_id

    read_course_name()
    read_title()
    read_staff()
    read_semester()
    read_author()
    read_summary()
    read_keywords()


if __name__ == "__main__":
    pass
    # analyze_document('document/example-2.pdf')
