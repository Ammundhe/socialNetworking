# Generated by Django 4.0.2 on 2022-02-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmedia',
            name='group_imges',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='groupmedia',
            name='group_videos',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
