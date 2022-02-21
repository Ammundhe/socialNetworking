# Generated by Django 4.0.2 on 2022-02-18 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelikes',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagelikes',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='page', to='page.page'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pagelikes',
            name='member',
        ),
        migrations.AddField(
            model_name='pagelikes',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
