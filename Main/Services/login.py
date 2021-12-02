from Main.forms import *
from Main.models import *


def login_admin(form):
    admins = Admin.objects.all()

    if form.is_valid():
        username = form['username'].value()
        password = form['password'].value()

        for admin in admins:
            if admin.username == username and admin.password == password:
                return True
    return False


def login_user(form):
    users = User.objects.all()

    if form.is_valid():
        username = form['username'].value()

        for user in users:
            if user.username == username:
                return True

    return False


def save_user_form(form, user):
    if form.is_valid():
        user.username = form['username'].value()

        user.save()
