from Main.models import *


def create_document(form, pk):
    document = Document()
    user =  User.objects.get(id=pk)
    if form.is_valid():
        document.user_id = user
        document.title = form['title'].value()
        document.document = form['document'].value()

        document.save()
