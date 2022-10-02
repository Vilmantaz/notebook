from django.contrib import admin
from .models import Category, Record


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'creation_date', 'category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Record, RecordAdmin)