# Generated by Django 4.0.2 on 2022-02-28 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_remove_page_pageimage_page_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='image',
        ),
    ]