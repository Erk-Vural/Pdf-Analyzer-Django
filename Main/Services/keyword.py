from Main.Models.Keyword import Keyword
from Main.Models.User import User


def create_keyword(pk, content):
    keyword = Keyword()
    user = User.objects.get(id=pk)

    keyword.user_id = user
    keyword.content = content

    keyword.save()


def read_keyword(pk):
    keyword = Keyword.objects.get(id=pk)
    return keyword


def delete_keyword(user_id, doc_id):
    keyword = read_keyword(pk)

    keyword.delete()