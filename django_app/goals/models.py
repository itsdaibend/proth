from django.conf import settings
from django.db import models


class Goal(models.Model):
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    expire_at = models.DateTimeField(blank=True)
    counter = models.PositiveIntegerField(default=0, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.description}"
