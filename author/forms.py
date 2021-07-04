from django import forms
from author.models import Author

class AddForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    patronymic = forms.CharField(max_length=20)