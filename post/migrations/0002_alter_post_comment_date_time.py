# Generated by Django 4.0.2 on 2022-02-28 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='date_time',
            field=models.DateField(default=datetime.date(2022, 2, 27)),
        ),
    ]