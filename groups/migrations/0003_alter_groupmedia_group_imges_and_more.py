# Generated by Django 4.0.2 on 2022-02-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_remove_groupmember_member_groupmember_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmedia',
            name='group_imges',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='groupmedia',
            name='group_videos',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]