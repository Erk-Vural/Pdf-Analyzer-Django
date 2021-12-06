from Main.Models.Title import Title
from Main.Models.User import User


def create_title(pk, content):
    title = Title()
    user = User.objects.get(id=pk)

    title.user_id = user
    title.content = content

    title.save()


def read_title(pk):
    title = Title.objects.get(id=pk)
    return title


def delete_title(user_id, doc_id):
    title = read_title(pk)

    title.delete()
