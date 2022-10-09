from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Category, Record

class RecordCreateForm(forms.ModelForm):

    # def __init__(self,*args, user=None, **kwargs):
    #     super(RecordCreateForm, self).__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Record
        fields = ['name', 'content', 'image', 'category',]
 