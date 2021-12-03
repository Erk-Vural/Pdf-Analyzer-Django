from django.shortcuts import render, redirect

from Main.forms import *
from Main.Services.login import *
from Main.Services.admin_panel import *
from Main.Services.user_panel import *


# Create your views here.

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
            return redirect('user-panel', is_exist)

    user_form = UserForm()

    context = {
        'admin_form': admin_form,
        'user_form': user_form
    }

    return render(request, "login.html", context)


def admin_panel_view(request):
    users = read_all_user()

    context = {
        'users': users,
    }

    return render(request, "admin-panel.html", context)


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


def document_create_view(request, pk):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        create_document(form, pk)

        return redirect('user-panel', pk)

    form = DocumentForm()

    context = {
        'pdf_form': form
    }

    return render(request, "document-create.html", context)


def document_delete_view(request, tk, pk):
    delete_document(pk)

    return redirect('user-panel', tk)
