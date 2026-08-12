from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):
    STUDENT = ("student", "Student")
    INSTRUCTOR = ("instructor", "Instructor")

class CustomUser(AbstractUser):
    role = models.CharField(choices=RoleChoices.choices, max_length=20)
    bio = models.TextField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photo")
    headline = models.CharField(max_length=50, null=True, blank=True)

    


