from django.contrib import admin
from .models import Category, Record, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'creation_date', 'category',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('display_category', 'record', 'user',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(User, UserAdmin)
