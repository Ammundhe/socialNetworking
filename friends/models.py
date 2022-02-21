from django.db import models
from django.contrib.auth.models import User

class Myuser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    friends=models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")

    def __str__(self) -> str:
        return str(self.friends)
