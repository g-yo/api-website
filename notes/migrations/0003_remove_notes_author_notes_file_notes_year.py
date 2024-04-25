# Generated by Django 5.0.3 on 2024-04-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_author_alter_notes_publish_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='author',
        ),
        migrations.AddField(
            model_name='notes',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='user_files/'),
        ),
        migrations.AddField(
            model_name='notes',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
    ]
