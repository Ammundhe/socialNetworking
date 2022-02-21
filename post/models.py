from django.db import models
from django.contrib.auth.models import User
from friends.models import Myuser

class Page(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField(null=True, blank=True)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    date=models.DateField()
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.title)
    
class MediaFiles(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="mediafiles")
    images=models.ImageField()
    videos=models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.post)

class Post_comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postcomment")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self) -> str:
        return str(self.user)