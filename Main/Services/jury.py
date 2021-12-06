from Main.Models.Document import Document
from Main.Models.JuryInfo import JuryInfo
from Main.Models.User import User


def create_jury_info(user_id, doc_id, name, last_name, title):
    jury_info = JuryInfo()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    jury_info.user_id = user
    jury_info.doc_id = document
    jury_info.name = name
    jury_info.last_name = last_name
    jury_info.title = title

    jury_info.save()


def read_jury_info(user_id, doc_id):
    jury_info = JuryInfo.objects.filter(user_id=user_id, doc_id=doc_id)
    return jury_info


def delete_jury_info(user_id, doc_id):
    jury_info = read_jury_info(user_id, doc_id)

    jury_info.delete()
