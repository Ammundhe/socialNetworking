# Generated by Django 4.0.2 on 2022-02-20 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_mediafiles_friend_post_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafiles',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediafiles', to='post.post'),
        ),
    ]
