# Generated by Django 4.0.2 on 2022-03-02 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_pagepost_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemedia',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PageMedia', to='page.page'),
        ),
    ]
