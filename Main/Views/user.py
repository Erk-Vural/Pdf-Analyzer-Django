from django.shortcuts import redirect, render

from Main.Services.document import read_all_documents_by_user
from Main.Services.user import create_user, delete_user, update_user
from Main.forms import UserForm


def user_create_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        create_user(user_form)

        return redirect('admin-panel')

    user_form = UserForm()

    context = {
        'user_form': user_form
    }

    return render(request, "user-create.html", context)


def user_delete_view(request, pk):
    delete_user(pk)

    return redirect('admin-panel')


def user_update_view(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        update_user(user_form, pk)

        return redirect('admin-panel')

    user_form = UserForm()

    context = {
        'user_form': user_form
    }

    return render(request, "user-create.html", context)


def user_panel_view(request, pk):
    documents = read_all_documents_by_user(pk)

    context = {
        'user_id': pk,
        'documents': documents
    }

    return render(request, "user-panel.html", context)
