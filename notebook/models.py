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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')

    def display_category(self):
        return ', '.join(category.name for category in self.category.all())


    def __str__(self):
            return f'{self.name} {self.content} {self.creation_date}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

# class UserCategory(models.Model):
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = 'User category'
#         verbose_name_plural = 'User categories'

# class UserRecord(models.Model):
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
#     record = models.ForeignKey('Record', on_delete=models.SET_NULL, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

 
            
#     def __str__(self):
#             return f'{self.category} {self.record}'