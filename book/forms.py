from django import forms
from django.core.exceptions import ValidationError

from author.models import Author
from .models import Book

class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors', 'cover']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 128:
            raise ValidationError('Довжина перевищує 128 знаків')
        return name

    def clean_count(self):
        count = self.cleaned_data['count']
        if count < 1:
            raise ValidationError('Додайте хоча б одну книжку')
        return count