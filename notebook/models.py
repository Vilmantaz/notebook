from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Pavadinimas', max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Record(models.Model):
    name = models.CharField('Pavadinimas', max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    image = models.ImageField('Paveikslėlis', upload_to='images', blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, related_name='category')

    def __str__(self):
            return f'{self.name} {self.content} {self.creation_date}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"
