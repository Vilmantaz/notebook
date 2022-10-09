from django.contrib import admin
from .models import Category, Record, Profile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'creation_date', 'category', 'user',)

# class UserRecordAdmin(admin.ModelAdmin):
#     list_display = ('category', 'record', 'user',)

# class UserCategoryAdmin(admin.ModelAdmin):
#     list_display = ('category', 'user',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Record, RecordAdmin)
# admin.site.register(UserRecord, UserRecordAdmin)
# admin.site.register(UserCategory, UserCategoryAdmin)
admin.site.register(Profile)
