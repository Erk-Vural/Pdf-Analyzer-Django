from Main.Models.Document import Document
from Main.Models.User import User


def create_document(form, pk):
    document = Document()
    user = User.objects.get(id=pk)
    if form.is_valid():
        document.user_id = user
        document.title = form['title'].value()
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
