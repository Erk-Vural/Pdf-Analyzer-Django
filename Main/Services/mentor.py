from Main.Models.Document import Document
from Main.Models.MentorInfo import MentorInfo
from Main.Models.User import User


def create_mentor_info(user_id, doc_id, name, last_name, title):
    mentor_info = MentorInfo()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    mentor_info.user_id = user
    mentor_info.doc_id = document
    mentor_info.name = name
    mentor_info.last_name = last_name
    mentor_info.title = title

    mentor_info.save()


def read_mentor_info(user_id, doc_id):
    mentor_info = MentorInfo.objects.filter(user_id=user_id, doc_id=doc_id)
    return mentor_info


def delete_mentor_info(user_id, doc_id):
    mentor_info = read_mentor_info(user_id, doc_id)

    mentor_info.delete()
