from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)


class PagePost(models.Model):
    page=models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=255)
    date=models.DateField()
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.title)

class PageMedia(models.Model):
    page=models.ForeignKey(Page, on_delete=models.CASCADE, related_name="PageMedia")
    Page_post=models.ForeignKey(PagePost, on_delete=models.CASCADE, related_name="PostMedia")
    Pageimges=models.ImageField(upload_to="media/", null=True, blank=True)
    Page_videos=models.FileField(upload_to="media/", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.Page_post)


class PageLikes(models.Model):
    page=models.ForeignKey(Page, on_delete=models.CASCADE, related_name="page")
    member=models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")
    def __str__(self) -> str:
        return str(self.page)
