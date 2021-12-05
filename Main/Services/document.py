from Main.Models.Document import *
from Main.Models.User import User


def create_course_name(pk, content):
    course_name = CourseName()
    user = User.objects.get(id=pk)

    course_name.user_id = user
    course_name.content = content

    course_name.save()


def create_mentor_info(pk, name, last_name, title):
    mentor_info = MentorInfo()
    user = User.objects.get(id=pk)

    mentor_info.user_id = user
    mentor_info.name = name
    mentor_info.last_name = last_name
    mentor_info.title = title

    mentor_info.save()


def create_jury_info(pk, name, last_name, title):
    jury_info = JuryInfo()
    user = User.objects.get(id=pk)

    jury_info.user_id = user
    jury_info.name = name
    jury_info.last_name = last_name
    jury_info.title = title

    jury_info.save()


def create_semester(pk, content):
    semester = Semester()
    user = User.objects.get(id=pk)

    semester.user_id = user
    semester.content = content

    semester.save()


def create_author(pk, name, last_name, student_number, education_type):
    author = Author()
    user = User.objects.get(id=pk)

    author.user_id = user
    author.name = name
    author.last_name = last_name
    author.student_number = student_number
    author.education_type = education_type

    author.save()


def create_document(form, pk):
    document = Document()
    user = User.objects.get(id=pk)
    if form.is_valid():
        document.user_id = user
        document.document = form['document'].value()

        document.save()


def read_all_documents():
    documents = Document.objects.all()

    return documents


def read_all_documents_by_user(user_id):
    documents = Document.objects.filter(user_id=user_id)

    return documents


def read_document(pk):
    document = Document.objects.get(id=pk)
    return document


def delete_document(pk):
    document = read_document(pk)

    document.delete()
