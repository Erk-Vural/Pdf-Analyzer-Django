from django.shortcuts import render

from Main.Services.author import read_author_by_user
from Main.Services.course_name import read_course_name_by_user
from Main.Services.document import read_documents_by_user, read_document
from Main.Services.keyword import read_keyword_by_user
from Main.Services.title import read_title_by_user
from Main.Services.semester import read_semester_by_user


def query1_home_view(request, pk):
    context = {
        'user_id': pk
    }

    return render(request, "query1.html", context)


def author_view(request, pk):
    authors = read_author_by_user(pk)
    context = {
        'user_id': pk,
        'datas': authors
    }

    return render(request, "query1.html", context)


def courseName_view(request, pk):
    course_name = read_course_name_by_user(pk)
    context = {
        'user_id': pk,
        'datas': course_name
    }

    return render(request, "query1.html", context)


def title_view(request, pk):
    title = read_title_by_user(pk)
    context = {
        'user_id': pk,
        'datas': title
    }

    return render(request, "query1.html", context)


def keyword_view(request, pk):
    keywords = read_keyword_by_user(pk)
    context = {
        'user_id': pk,
        'datas': keywords
    }

    return render(request, "query1.html", context)


def semester_view(request, pk):
    semester = read_semester_by_user(pk)
    context = {
        'user_id': pk,
        'datas': semester
    }

    return render(request, "query1.html", context)


def query_list_view(request, tk, pk):
    documents = read_document(tk, pk)

    context = {
        'user_id': tk,
        'doc_id': pk,
        'documents': documents
    }

    return render(request, "query-list.html", context)