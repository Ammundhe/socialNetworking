# Generated by Django 4.0.2 on 2022-02-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_pagelikes_admin_pagelikes_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemedia',
            name='Page_videos',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='pagemedia',
            name='Pageimges',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]