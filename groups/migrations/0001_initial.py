# Generated by Django 4.0.2 on 2022-02-17 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_imges', models.ImageField(blank=True, null=True, upload_to='')),
                ('group_videos', models.FileField(blank=True, null=True, upload_to='')),
                ('group_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.grouppost')),
            ],
        ),
    ]
