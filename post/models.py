from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField()
    date=models.DateField()
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.title)
    
class MediaFiles(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    images=models.ImageField(null=True, blank=True)
    videos=models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.post)
