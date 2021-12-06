from Main.Models.Document import Semester
from Main.Models.User import User


def create_semester(pk, content):
    semester = Semester()
    user = User.objects.get(id=pk)

    semester.user_id = user
    semester.content = content

    semester.save()


def read_semester(pk):
    semester = Semester.objects.get(id=pk)
    return semester


def delete_semester(pk):
    semester = read_semester(pk)

    semester.delete()
