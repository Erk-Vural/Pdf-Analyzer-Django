from django.shortcuts import redirect, render

from Main.Services.document import delete_document, create_document
from Main.document_analyzer import read_text
from Main.forms import DocumentForm


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
