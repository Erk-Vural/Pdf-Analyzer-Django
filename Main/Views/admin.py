from django.shortcuts import render

from Main.Services.user import read_all_user


def admin_panel_view(request):
    users = read_all_user()

    context = {
        'users': users,
    }

    return render(request, "admin-home.html", context)