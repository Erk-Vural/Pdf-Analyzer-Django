from Main.Models.Document import Document
from Main.Models.Author import Author
from Main.Models.User import User


def create_author(user_id, doc_id, name, last_name, student_number, education_type):
    author = Author()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    author.user_id = user
    author.doc_id = document
    author.name = name
    author.last_name = last_name
    author.student_number = student_number
    author.education_type = education_type

    author.save()


def read_author(user_id, doc_id):
    author = Author.objects.filter(user_id=user_id, doc_id=doc_id)
    return author


def delete_author(user_id, doc_id):
    author = read_author(user_id, doc_id)

    author.delete()
