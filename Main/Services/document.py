import os

from Main.Models.Document import *
from Main.Models.User import User

BASE = os.path.dirname(os.path.abspath(__file__))


def create_mentor_info(pk, name, last_name, title):
    mentor_info = MentorInfo()
    user = User.objects.get(id=pk)

    mentor_info.user_id = user
    mentor_info.name = name
    mentor_info.last_name = last_name
    mentor_info.title = title

    mentor_info.save()


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

    local_pdf_filename = '../static/Main/documents/' + document.document.name
    os.remove(os.path.join(BASE, local_pdf_filename))
    document.delete()