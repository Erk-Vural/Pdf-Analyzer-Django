from django.shortcuts import render, redirect

from Main.forms import *
from Main.models import *
from Main.Services.login import *


# Create your views here.

def login_view(request):
    is_admin_exist = False

    if request.method == 'POST':
        admin_form = AdminForm(request.POST)
        is_admin_exist = login_admin(admin_form)

        if is_admin_exist:
            return redirect('admin-panel')

    admin_form = AdminForm()

    is_user_exist = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        is_user_exist = login_user(user_form)

        if is_user_exist:
            return redirect('user-panel')

    user_form = UserForm()

    context = {
        'admin_form': admin_form,
        'user_form': user_form
    }

    return render(request, "login.html", context)


def admin_panel_view(request):
    context = {
    }

    return render(request, "admin-panel.html", context)


def user_panel_view(request):
    context = {
    }

    return render(request, "user-panel.html", context)
