from django import forms


class AdminForm(forms.Form):
    username = forms.CharField(label="Username ")
    password = forms.CharField(label="Password ")


class UserForm(forms.Form):
    username = forms.CharField(label="Username ")


class DocumentForm(forms.Form):
    document = forms.FileField(label='Document', required="false")
