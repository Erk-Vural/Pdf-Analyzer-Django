from django.shortcuts import redirect, render

from Main.Services.document import delete_document, create_document
from Main.Services.project import delete_project
from Main.document_analyzer import analyze_document
from Main.forms import DocumentForm


def document_create_view(request, pk):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        create_document(form, pk)

        filename = form['document'].value().name
        analyze_document(filename, pk)

        return redirect('user-panel', pk)

    form = DocumentForm()

    context = {
        'pdf_form': form
    }

    return render(request, "document-create.html", context)


def document_delete_view(request, tk, pk):
    delete_project(tk, pk)

    return redirect('user-panel', tk)
