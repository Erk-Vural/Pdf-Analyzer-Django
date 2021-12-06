from Main.Models.MentorInfo import MentorInfo
from Main.Models.User import User


def create_mentor_info(pk, name, last_name, title):
    mentor_info = MentorInfo()
    user = User.objects.get(id=pk)

    mentor_info.user_id = user
    mentor_info.name = name
    mentor_info.last_name = last_name
    mentor_info.title = title

    mentor_info.save()


def read_mentor_info(pk):
    mentor_info = MentorInfo.objects.get(id=pk)
    return mentor_info


def delete_mentor_info(user_id, doc_id):
    mentor_info = read_mentor_info(pk)

    mentor_info.delete()
