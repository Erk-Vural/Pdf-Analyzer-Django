from Main.Models.Admin import Admin


def login_admin(form):
    admins = Admin.objects.all()

    if form.is_valid():
        username = form['username'].value()
        password = form['password'].value()

        for admin in admins:
            if admin.username == username and admin.password == password:
                return True
    return False
