from Main.Models.Document import CourseName
from Main.Models.User import User


def create_course_name(pk, content):
    course_name = CourseName()
    user = User.objects.get(id=pk)

    course_name.user_id = user
    course_name.content = content

    course_name.save()


def read_course_name(pk):
    course_name = CourseName.objects.get(id=pk)
    return course_name


def delete_course_name(pk):
    course_name = read_course_name(pk)

    course_name.delete()
