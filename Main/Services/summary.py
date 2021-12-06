from Main.Models.Document import Summary
from Main.Models.User import User


def create_summary(pk, content):
    summary = Summary()
    user = User.objects.get(id=pk)

    summary.user_id = user
    summary.content = content

    summary.save()


def read_summary(pk):
    summary = Summary.objects.get(id=pk)
    return summary


def delete_summary(pk):
    summary = read_summary(pk)

    summary.delete()
