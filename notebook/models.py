from django.db import models
from tinymce.models import HTMLField

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
            return f'{self.name} {self.creation_date}'