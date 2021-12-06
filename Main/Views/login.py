# Create your views here.
from django.shortcuts import redirect, render

from Main.Services.admin import login_admin
from Main.Services.user import login_user
from Main.forms import AdminForm, UserForm


def login_view(request):
    if request.method == 'POST':
        admin_form = AdminForm(request.POST)
        is_exist = login_admin(admin_form)

        if is_exist:
            return redirect('admin-panel')

    admin_form = AdminForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        is_exist = login_user(user_form)

        if is_exist != 0:
            return redirect('user-home', is_exist)

    user_form = UserForm()

    context = {
        'admin_form': admin_form,
        'user_form': user_form
    }

    return render(request, "login.html", context)