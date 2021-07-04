from django import forms
from django.core.exceptions import ValidationError

from .models import Order
import datetime

class AddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'book']


class EditForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['end_at', 'plated_end_at']

    def clean_end_at(self):
        print(self.__dict__)
        print(self.data['end_at'])
        plated_end_at = datetime.datetime.strptime(self.data['plated_end_at'][0:18], '%Y-%m-%d %H:%M:%S')
        end_at = datetime.datetime.strptime(self.data['end_at'][0:18], '%Y-%m-%d %H:%M:%S')
        if end_at > plated_end_at:
            raise ValidationError('Термін повернення прострочено. Або змініть термін повернення або платіть штраф')
        return self.cleaned_data['end_at']
