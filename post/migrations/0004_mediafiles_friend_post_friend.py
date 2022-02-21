# Generated by Django 4.0.2 on 2022-02-20 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
        ('post', '0003_alter_mediafiles_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafiles',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='friends.myuser'),
        ),
        migrations.AddField(
            model_name='post',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='friends.myuser'),
        ),
    ]
