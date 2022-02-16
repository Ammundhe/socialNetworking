from django.db import models
from django.contrib.auth.models import User

class Myuser(models.Model):
    friend=models.ManyToManyField(User)

    def __str__(self) -> str:
        return str(self.friend)
