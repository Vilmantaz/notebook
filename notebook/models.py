from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Pavadinimas', max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Record(models.Model):
    name = models.CharField('Pavadinimas', max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
            return f'{self.name} {self.content} {self.creation_date}'

class User(models.Model):
    category = models.ManyToManyField('Category')
    record = models.ForeignKey('Record', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def display_category(self):
            return ', '.join(category.name for category in self.category.all())
            
    def __str__(self):
            return f'{self.category} {self.record}'