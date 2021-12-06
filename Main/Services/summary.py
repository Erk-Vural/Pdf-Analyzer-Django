from Main.Models.Document import Document
from Main.Models.Summary import Summary
from Main.Models.User import User


def create_summary(user_id, doc_id, content):
    summary = Summary()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    summary.user_id = user
    summary.doc_id = document
    summary.content = content

    summary.save()


def read_summary(user_id, doc_id):
    summary = Summary.objects.get(user_id=user_id, doc_id=doc_id)
    return summary


def delete_summary(user_id, doc_id):
    summary = read_summary(user_id, doc_id)

    summary.delete()
