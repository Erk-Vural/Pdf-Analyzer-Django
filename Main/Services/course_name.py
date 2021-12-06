from Main.Models.Document import Document
from Main.Models.CourseName import CourseName
from Main.Models.User import User


def create_course_name(user_id, doc_id, content):
    course_name = CourseName()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    course_name.user_id = user
    course_name.doc_id = document
    course_name.content = content

    course_name.save()


def read_course_name_by_user(user_id):
    course_name = CourseName.objects.filter(user_id=user_id)
    return course_name


def read_course_name(user_id, doc_id):
    course_name = CourseName.objects.filter(user_id=user_id, doc_id=doc_id)
    return course_name


def delete_course_name(user_id, doc_id):
    course_name = read_course_name(user_id, doc_id)

    course_name.delete()
