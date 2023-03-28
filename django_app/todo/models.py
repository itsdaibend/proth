from django.conf import settings
from django.db import models


class TodoLabel(models.Model):
    label = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"

    def __str__(self):
        return f"{self.label}"


class Todo(models.Model):
    class Priority(models.TextChoices):
        LOW = "1", "LOW"
        MEDIUM = "2", "MEDIUM"
        HIGH = "3", "HIGH"
        EXTRA_HIGH = "4", "EXTRA HIGH"

    class Status(models.TextChoices):
        TODO = "1", "TODO"
        IN_PROGRESS = "2", "IN PROGRESS"
        ON_HOLD = "3", "ON HOLD"
        COMPLETE = "4", "COMPLETE"

    DEFAULT_LABEL_ID = 1  # 'Other'

    title = models.CharField(max_length=150)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    label = models.ForeignKey(
        TodoLabel, default=DEFAULT_LABEL_ID, on_delete=models.CASCADE
    )
    priority = models.CharField(
        max_length=2, choices=Priority.choices, default=Priority.MEDIUM
    )
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.TODO)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.title}"
