# Generated by Django 4.0.2 on 2022-02-18 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmember',
            name='member',
        ),
        migrations.AddField(
            model_name='groupmember',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='groups.group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupmember',
            name='group_member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
