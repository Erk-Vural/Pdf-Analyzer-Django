from django import forms


class AdminForm(forms.Form):
    username = forms.CharField(label="Username: ")
    password = forms.CharField(label="Password: ")


class UserForm(forms.Form):
    username = forms.CharField(label="Username: ")


class DocumentForm(forms.Form):
    title = forms.CharField(label="Title", required="false")
    document = forms.FileField(label='Document', required="false")
