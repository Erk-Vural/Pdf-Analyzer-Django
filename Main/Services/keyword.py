from Main.Models.Document import Document
from Main.Models.Keyword import Keyword
from Main.Models.User import User


def create_keyword(user_id, doc_id, content):
    keyword = Keyword()
    user = User.objects.get(id=user_id)
    document = Document.objects.get(id=doc_id)

    keyword.user_id = user
    keyword.doc_id = document
    keyword.content = content

    keyword.save()


def read_keyword(user_id, doc_id):
    keyword = Keyword.objects.filter(user_id=user_id, doc_id=doc_id)
    return keyword


def delete_keyword(user_id, doc_id):
    keyword = read_keyword(user_id, doc_id)

    keyword.delete()
