from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="Userprofile")
    profile_picture=models.ImageField(upload_to="profilePicture/", null=True, blank=True)
    address=models.TextField()
    mobile=models.CharField(max_length=12)
    
