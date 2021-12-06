from Main.Models.Document import Document
from Main.Models.Title import Title
from Main.Models.User import User


def create_title(user_id, doc_id, content):
    title = Title()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    title.user_id = user
    title.doc_id = document
    title.content = content

    title.save()


def read_title(user_id, doc_id):
    title = Title.objects.filter(user_id=user_id, doc_id=doc_id)
    return title


def delete_title(user_id, doc_id):
    title = read_title(user_id, doc_id)

    title.delete()
