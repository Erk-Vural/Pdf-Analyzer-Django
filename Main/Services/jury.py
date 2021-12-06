from Main.Models.Document import JuryInfo
from Main.Models.User import User


def create_jury_info(pk, name, last_name, title):
    jury_info = JuryInfo()
    user = User.objects.get(id=pk)

    jury_info.user_id = user
    jury_info.name = name
    jury_info.last_name = last_name
    jury_info.title = title

    jury_info.save()


def read_jury_info(pk):
    jury_info = JuryInfo.objects.get(id=pk)
    return jury_info


def delete_jury_info(pk):
    jury_info = read_jury_info(pk)

    jury_info.delete()
