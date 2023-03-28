from django.contrib.auth.models import AbstractUser
from django.db import models


class RegularUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.username} ( {self.email} )"
