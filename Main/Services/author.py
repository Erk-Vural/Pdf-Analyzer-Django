from Main.Models.Document import Author
from Main.Models.User import User


def create_author(pk, name, last_name, student_number, education_type):
    author = Author()
    user = User.objects.get(id=pk)

    author.user_id = user
    author.name = name
    author.last_name = last_name
    author.student_number = student_number
    author.education_type = education_type

    author.save()


def read_author(pk):
    author = Author.objects.get(id=pk)
    return author


def delete_author(pk):
    author = read_author(pk)

    author.delete()
