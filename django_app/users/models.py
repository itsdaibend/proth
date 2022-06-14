from django.db import models

from django.contrib.auth.models import AbstractUser

class RegularUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.username} ( {self.email} )'