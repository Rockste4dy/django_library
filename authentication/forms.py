from django import forms
from authentication.models import CustomUser

class AddForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    middle_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=128)
    role = forms.IntegerField()
    is_active = forms.BooleanField(required=False)