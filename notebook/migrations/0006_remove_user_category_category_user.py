# Generated by Django 4.1.1 on 2022-10-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_rename_usersrecord_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ManyToManyField(to='notebook.user'),
        ),
    ]
