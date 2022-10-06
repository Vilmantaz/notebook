from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Category, Record

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError(f'Vartotojo vardas {data} užimtas!')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError(f'El. paštas {data} užimtas!')
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        if password != password2:
            raise ValidationError('Slaptažodžiai nesutampa!')

class RecordCreateForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['name', 'content', 'image', 'category']
 