from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Category, Record, UserCategory

# class UserCategoryCreateForm(forms.ModelForm):
#     class Meta:
#         model = UserCategory
#         fields = ['user', 'category']
#         widgets = {'user': forms.HiddenInput()}