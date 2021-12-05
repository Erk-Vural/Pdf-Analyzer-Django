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

block = ""
person_1 = ""
person_2 = ""
person_3 = ""
persons_info = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

semester = ""


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


def read_persons():
    read_block()
    find_persons()
    parse_persons_info(person_1, 0)
    parse_persons_info(person_2, 1)
    parse_persons_info(person_3, 2)
    save_persons_info()


def read_block():
    global block
    pages = [1]

    extracted_text = read_text(pages)

    start_point = extracted_text.find(title) + len(title) + 4
    end_point = start_point + 64

    temp_area = extracted_text[start_point: end_point]

    start_point = 0
    end_point = temp_area.find("   ")

    temp = temp_area[start_point: end_point]

    start_point = extracted_text.find(temp) + len(title) + 4

    block = extracted_text[start_point:]


def find_persons():
    global person_1
    global person_2
    global person_3

    info = block

    info = info.replace("...", "")
    info = info.replace("..", "")
    info = info.replace("Kocaeli Üniv.", "")
    end_point = info.find("Tezin") - 5
    info = info[:end_point]

    end_point = info.find(",")
    person_1 = info[:end_point]
    info = info[end_point + 4:]

    end_point = info.find(",")
    person_2 = info[3:end_point]
    info = info[end_point + 4:]

    end_point = info.find(",")
    person_3 = info


def parse_persons_info(person, person_index):
    title_str = ""
    name_str = ""
    last_name_str = ""
    duty_str = ""

    while person.find(".") != -1:
        point = person.find(".")
        title_str = title_str + person[:point]
        person = person[point + 1:]

    if person.find("Danışman") != -1:
        point = person.find("Danışman")
        person = person[:point]
        duty_str = "Danışman"

    elif person.find("Jüri") != -1:
        point = person.find("Jüri Üyesi")
        person = person[:point - 1]
        duty_str = "Jüri Üyesi"

    person = person[1:]

    point = person.find(" ")
    name_str = person[:point]
    last_name_str = person[point + 1:]

    persons_info[person_index][0] = title_str
    persons_info[person_index][1] = name_str
    persons_info[person_index][2] = last_name_str
    persons_info[person_index][3] = duty_str


def save_persons_info():
    for i in range(3):
        if persons_info[i][3] == "Danışman":
            pass
            # create_mentor_info(4, persons_info[i][1], persons_info[i][2], persons_info[i][0])
        # create_jury_info(4, persons_info[i][1], persons_info[i][2], persons_info[i][0])


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
    pass


if __name__ == "__main__":
    read_course_name()
    read_title()
    read_persons()
    read_semester()
    read_author()
