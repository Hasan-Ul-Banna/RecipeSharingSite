from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="media/images/profile_picture", null=True, blank=True)
    about = models.TextField(blank=True)
