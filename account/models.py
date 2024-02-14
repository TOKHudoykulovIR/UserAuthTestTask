from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='account_photos/', null=True, blank=True)
    description = models.TextField(max_length=256, null=True, blank=True)


class Comment(models.Model):
    to = models.ForeignKey("CustomUser", on_delete=models.CASCADE, related_name="received_comments")
    author = models.ForeignKey("CustomUser", on_delete=models.CASCADE, related_name="left_comments")
    text = models.CharField(max_length=100)
