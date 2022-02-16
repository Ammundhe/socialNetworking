from tokenize import group
from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)


class GroupPost(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    date=models.DateField()
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.title)

class GroupMedia(models.Model):
    group_post=models.ForeignKey(GroupPost, on_delete=models.CASCADE)
    group_imges=models.ImageField(null=True, blank=True)
    group_videos=models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.group_post)


class GroupMember(models.Model):
    member=models.ManyToManyField(User)

    def __str__(self) -> str:
        return str(self.admin)
