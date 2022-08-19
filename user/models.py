from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="images/profile_picture", null=True, blank=True)


user_model = get_user_model()

class Subscribe(models.Model):
    subscribed_by = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='subscribed_by')
    subscribed_to = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='subscribed_to')

    class Meta:
        unique_together = ["subscribed_by", "subscribed_to"]

class ReportUser(models.Model):
    reported_by = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='reported_by')
    reported_to = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='reported_to')
    report_reason = models.TextField(blank=True)
