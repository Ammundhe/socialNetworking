# Generated by Django 4.0.2 on 2022-02-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_page_pageimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='pageImage',
        ),
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mypage'),
        ),
    ]