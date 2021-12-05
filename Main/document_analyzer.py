# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

from pdfminer import high_level

# Path of tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different


def read_text(pages):
    local_pdf_filename = '../static/Main/documents/example-2.pdf'

    extracted_text = high_level.extract_text(local_pdf_filename, "", pages)

    if extracted_text == "":
        read_image()

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


course_name = ""
title = ""

staff_info_block = ["", "", ""]

semester = ""

authors_info_block = ["", "", ""]

summary = ""

keywords = []


def read_course_name():
    global course_name

    pages = [1]
    extracted_text = read_text(pages)

    if extracted_text.find('BİTİRME ÇALIŞMASI') != -1:
        course_name = 'BİTİRME ÇALIŞMASI'

    elif extracted_text.find('ARAŞTIRMA PROBLEMLERİ') != -1:
        course_name = 'ARAŞTIRMA PROBLEMLERİ'

    # create_course_name(4, result)


def read_title():
    global title
    pages = [1]

    extracted_text = read_text(pages)

    start_point = extracted_text.find(course_name) + len(course_name) + 4
    end_point = start_point + 64

    title_area = extracted_text[start_point: end_point]

    start_point = 0
    end_point = title_area.find("   ")

    title = title_area[start_point: end_point]

    # create_title(4, result)


def read_staff():
    pages = [1]

    extracted_text = read_text(pages)

    start_point = extracted_text.find(title) + len(title) + 4
    end_point = start_point + 64

    temp_area = extracted_text[start_point: end_point]

    start_point = 0
    end_point = temp_area.find("   ")

    temp = temp_area[start_point: end_point]

    start_point = extracted_text.find(temp) + len(title) + 4

    info = extracted_text[start_point:]

    info = info.replace("...", "")
    info = info.replace("..", "")
    info = info.replace("Kocaeli Üniv.", "")
    end_point = info.find("Tezin") - 5
    info = info[:end_point]

    end_point = info.find(",")
    staff_info_block[0] = info[:end_point]
    info = info[end_point + 4:]

    end_point = info.find(",")
    staff_info_block[1] = info[3:end_point]
    info = info[end_point + 4:]

    end_point = info.find(",")
    staff_info_block[2] = info

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
            # create_mentor_info(4, name_str, last_name_str, title_str)
        # create_jury_info(4, name_str, last_name_str, title_str)


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

    # create_semester(4, semester)


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

            point = name_last_name.find(" ")
            name = name_last_name[0:point]
            last_name = name_last_name[point:]

            # create_author(4, name, last_name, student_num, "1")

        else:
            continue


def read_summary():
    global summary
    pages = [6, 7, 8, 9, 10, 11]

    extracted_text = read_text(pages)

    start_point = extracted_text.find("ÖZET") + 4
    end_point = extracted_text.find("Anahtar") - 2
    summary = extracted_text[start_point:end_point]

    # create_summary(4, summary)


def read_keywords():
    global keywords
    # range is wider for decrease missing wanted part of data
    pages = [6, 7, 8, 9, 10, 11]

    extracted_text = read_text(pages)

    start_point = extracted_text.find("Anahtar Kelimeler:") + 19
    end_point = extracted_text.find("ABSTRACT")
    keywords_str = extracted_text[start_point:end_point]

    while keywords_str.find(",") != -1:
        point = keywords_str.find(",") + 2
        keyword = keywords_str[:point - 3]
        keywords_str = keywords_str[point:]

        keywords.append(keyword)

    # Get last keyword
    if keywords_str.find(",") == -1:
        point = keywords_str.find(" ")
        keyword = keywords_str[:point]

        keywords.append(keyword)

    for i in range(len(keywords)):
        pass
        # create_keyword(4, keywords[i])


if __name__ == "__main__":
    read_course_name()
    read_title()
    read_staff()
    read_semester()
    read_author()
    read_summary()
    read_keywords()
