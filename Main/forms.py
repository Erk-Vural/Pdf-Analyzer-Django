from django import forms
from django.forms import ModelForm

from Main.models import Document


class AdminForm(forms.Form):
    username = forms.CharField(label="Username: ")
    password = forms.CharField(label="Password: ")


class UserForm(forms.Form):
    username = forms.CharField(label="Username: ")


class DocumentForm(forms.Form):
    title = forms.CharField(label="Title", required="false")
    document = forms.FileField(label='Document', required="false")
