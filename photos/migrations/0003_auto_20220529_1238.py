# Generated by Django 3.2 on 2022-05-29 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_location_name_location_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='name',
        ),
    ]
