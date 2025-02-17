# Generated by Django 5.0.3 on 2024-04-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_rename_title_notes_place_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='Place',
            new_name='place',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='desription',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='genre',
        ),
        migrations.AddField(
            model_name='notes',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='notes',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
