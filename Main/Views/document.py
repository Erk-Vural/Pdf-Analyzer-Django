from django.shortcuts import redirect, render

from Main.Services.author import read_author
from Main.Services.course_name import read_course_name
from Main.Services.document import create_document
from Main.Services.jury import read_jury_info
from Main.Services.keyword import read_keyword
from Main.Services.mentor import read_mentor_info
from Main.Services.project import delete_project
from Main.Services.semester import read_semester
from Main.Services.summary import read_summary
from Main.Services.title import read_title
from Main.document_analyzer import analyze_document
from Main.forms import DocumentForm


def document_create_view(request, pk):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        doc_id = create_document(form, pk)
        filename = form['document'].value().name
        analyze_document(filename, pk, doc_id)

        return redirect('user-panel', pk)

    form = DocumentForm()

    context = {
        'pdf_form': form,
        'user_id': pk
    }

    return render(request, "document-create.html", context)


def document_delete_view(request, tk, pk):
    delete_project(tk, pk)

    return redirect('user-panel', tk)


def document_detail_view(request, tk, pk):
    authors = read_author(tk, pk)
    course_name = read_course_name(tk, pk)
    jury_infos = read_jury_info(tk, pk)
    mentor_infos = read_mentor_info(tk, pk)
    keywords = read_keyword(tk, pk)
    semester = read_semester(tk, pk)
    summary = read_summary(tk, pk)
    title = read_title(tk, pk)

    context = {
        'user_id': tk,
        'authors': authors,
        'course_name': course_name,
        'jury_infos': jury_infos,
        'mentor_infos': mentor_infos,
        'keywords': keywords,
        'semester': semester,
        'summary': summary,
        'title': title
    }

    return render(request, "document-detail.html", context)
