# Generated by Django 4.0.2 on 2022-02-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_mediafiles_images_alter_mediafiles_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]