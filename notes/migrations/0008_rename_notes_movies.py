# Generated by Django 5.0.3 on 2024-04-23 12:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_notes_genre_alter_notes_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Movies',
        ),
    ]
