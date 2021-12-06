from Main.Models.Document import Document
from Main.Models.Semester import Semester
from Main.Models.User import User


def create_semester(user_id, doc_id, content):
    semester = Semester()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    semester.user_id = user
    semester.doc_id = document
    semester.content = content

    semester.save()


def read_semester_by_user(user_id):
    semester = Semester.objects.filter(user_id=user_id)
    return semester


def read_semester(user_id, doc_id):
    semester = Semester.objects.filter(user_id=user_id, doc_id=doc_id)
    return semester


def delete_semester(user_id, doc_id):
    semester = read_semester(user_id, doc_id)

    semester.delete()
